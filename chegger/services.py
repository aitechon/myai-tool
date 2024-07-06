from google.generativeai import configure
import config
import google.generativeai as genai

# Load the API key from the environment variable
configure(api_key="AIzaSyCW6IjnbUl7UxuWjQGsbgI_WgKUFsuSW2k")

# Initialize the GenerativeModel object
model = genai.GenerativeModel("gemini-1.5-flash")

extra = "You are a highly knowledgeable AI tutor. You provide detailed, accurate, and concise answers to questions. Please answer the following question as if you were explaining to a student"


def generate_answer(question):
    """Sends the user question to the Gemini API and returns the answer."""
    response = model.generate_content(
        extra + question
    )  # Assuming 'predict' is the correct method
    return response.text  # Assuming the response object has a 'text' attribute
