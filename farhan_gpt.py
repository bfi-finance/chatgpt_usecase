# Import required libraries
import openai
import dotenv
import os

# Load the API key from .env file
dotenv.load_dotenv(dotenv_path='config/key.env')

# Create a class MyGPT
class MyGPT:

    # Constructor to set up API key
    def __init__(self):
        openai.api_key = os.environ['key']

    # Method to get response from GPT-3 model
    def _input_text(self, text: str) -> str:

        # Use openai.ChatCompletion.create() to get response
        chatgpt_model = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": text
            }]
        )

        # Get the response from the model
        chatgpt_model_response_str = chatgpt_model.choices[0].message.content.strip()

        # Return the response
        return chatgpt_model_response_str