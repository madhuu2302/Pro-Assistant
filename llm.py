
import os
from google import genai
from dotenv import load_dotenv

from prompt_template import get_prompt

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Gemini API key not found. Add GEMINI_API_KEY to your .env file."
    )

client = genai.Client(api_key=api_key)


def generate_response(user_input, template_name="General Question"):
    try:
        prompt = get_prompt(template_name, user_input)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if response.text:
            return response.text

        return "No response was generated. Please try again."

    except Exception as e:
        return f"Error generating response: {e}"

