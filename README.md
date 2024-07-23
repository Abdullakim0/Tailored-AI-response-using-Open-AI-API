# Mountain Spring Water AI
# Introduction
Mountain Spring Water AI is a Flask application designed to provide users with comprehensive information about Mountain Spring Water, including details about its sources, purification methods, 
and recommended usage. This web uses the OpenAI API to generate responses. If you hit API rate limits or quotas, it will fall back to pre-defined mock responses from a local file.

# Setup Instructions
Follow these steps to get Mountain Spring Water AI up and running:

1. Prepare Your Environment
Install Python and Flask:

Make sure you have Python installed on your system. If not, you can download it from python.org.

Install the necessary packages using pip:


pip install flask openai
Obtain Your OpenAI API Key:

Sign up or log in to OpenAI's platform.
Go to the API keys section and copy your API key.
2. Set Up the Flask Application
Create Your Project Directory:

Set up a new directory for your project:


mkdir mountain_spring_water_ai
cd mountain_spring_water_ai
Create the Flask Application File:

In your project directory, create a file named test.py. This file will contain the code for your Flask application and integrate with the OpenAI API. Replace 'open-api-key' with your actual API key.
Create the Mock Response File:

Create a file named responses.txt in the same directory as test.py. This file will hold predefined responses to use when the API quota is exceeded. Here's an example of what you might 
include in responses.txt:


What is this product?
- Mountain Spring Water is a premium bottled water sourced from pristine mountain springs. It is known for its purity and natural taste.

What does it contain?
- Mountain Spring Water contains 100% pure spring water with no additives or preservatives.

For whom is this product recommended?
- This product is ideal for health-conscious individuals, athletes, and anyone who prefers high-quality, natural water.
Create a Simple HTML Template:

Create a folder named templates in your project directory.
Inside the templates folder, create a file named home.html. This file will provide a basic user interface for interacting with the Flask application.
3. Run the Flask Application
Start the Flask Server:

From your project directory, run the Flask application:


python test.py
This will start a local development server accessible at http://127.0.0.1:5000/.

Test the Application:

Open a web browser and go to http://127.0.0.1:5000/.
Use the form to ask questions. The application will either fetch responses from the OpenAI API or use the mock responses from responses.txt if there are issues with the API quota.
