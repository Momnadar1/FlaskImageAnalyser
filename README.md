# FlaskImageAnalyser

1. The search_and_analyze endpoint allows you to search for images on a social network using a specified keyword and receive machine learning analysis results.
2. The upload_and_analyze endpoint enables you to upload an image file and receive machine learning analysis results.


## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.11.0 installed
- Pip (Python package installer) installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Momnadar1/FlaskImageAnalyser.git
    ```

2. Change into the project directory:

    ```bash
    cd your-project
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Set Up Environment Variables

Create a `.env` file in the project root and add the following content:

```plaintext
# Add any other necessary environment variables
YOUR_SOCIAL_NETWORK_API_KEY=your_social_network_api_key
YOUR_ML_MODEL_API_KEY=your_ml_model_api_key
```

### Making API Requests

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"keyword": "mountains"}' http://127.0.0.1:5000/search_and_analyze
    ```

    ```bash
    curl -X POST -F "image=@/path/to/your/image.jpg" http://127.0.0.1:5000/upload_and_analyze
    ```"# FlaskImageAnalyser" 
