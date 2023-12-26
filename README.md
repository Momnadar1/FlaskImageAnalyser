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
YOUR_USERNAME='insta_username'
YOUR_PASSWORD='insta_password'
```

### Making API Requests

    curl -X POST -H "Content-Type: application/json" -d '{"keyword": "mountains"}' http://127.0.0.1:5000/search_and_analyze

    curl -X POST -F "image=@/path/to/your/image.jpg" http://127.0.0.1:5000/upload_and_analyze
