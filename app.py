from dotenv import load_dotenv
import os 
from instagrapi import Client
from flask import Flask, render_template, request, jsonify
import requests
from PIL import Image
import io
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import json
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return {'status':'app is running'}
 
@app.route('/search_and_analyze', methods=['POST'])
def search_and_analyze():
    data = request.get_json()
    keyword = data.get('keyword')
    print('keyword', keyword)
    images = []

    if keyword:

        images = social_network_crawler(keyword)
        print(images)

        results = ml_model(images)
    else:
        results = None

    return results

@app.route('/upload_and_analyze', methods=['POST'])
def upload_and_analyze():
    image_file = request.files.get('image')
    # print('image_file', image_file, request.files.keys())
    results = ml_model_from_image(image_file)

    return results

def social_network_crawler(keyword):
    cl = Client()
    print(os.environ.get('YOUR_USERNAME'), os.environ.get('YOUR_PASSWORD'))
    cl.login(os.environ.get('YOUR_USERNAME'), os.environ.get('YOUR_PASSWORD'))

    medias = cl.hashtag_medias_top(keyword, amount=7)

    image_urls = [(json.loads(item.model_dump_json()))['thumbnail_url'] for item in medias]

    images = [download_image(url) for url in image_urls]
    print(images)
    return images

def ml_model(images):
    results = {'predictions': []}

    model = MobileNetV2(weights='imagenet')
    print('images', images)
    for image in images:
        print(image)
        if image:
            name = image
            image = io.BytesIO(open(image, 'rb').read())
            img_array = np.array(Image.open(image).resize((224, 224)))
            img_array = preprocess_input(img_array.reshape(1, 224, 224, 3))

            predictions = model.predict(img_array)

            decoded_predictions = decode_predictions(predictions)

            results['predictions'].append(decoded_predictions[0][0][1])
            os.remove(name)

    return results

def ml_model_from_image(image_file):
    results = {'predictions': []}

    model = MobileNetV2(weights='imagenet')
    print(image_file)
    
    if image_file:
        print(image_file)
        img_array = np.array(Image.open(image_file).resize((224, 224)))
        img_array = preprocess_input(img_array.reshape(1, 224, 224, 3))

        predictions = model.predict(img_array)

        decoded_predictions = decode_predictions(predictions)

        results['predictions'].append(decoded_predictions[0][0][1])

    return results

def download_image(url):
    try:

        response = requests.get(url)


        if response.status_code == 200:
    
            image = Image.open(io.BytesIO(response.content))
            image.save(url.split('?')[0].split('/')[-1])
            return url.split('?')[0].split('/')[-1]
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
