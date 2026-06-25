import os
from dotenv import load_dotenv
from google import genai
from prompts import EXTRACTION_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_info(text):
    prompt = EXTRACTION_PROMPT.format(text=text)

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",  # use your working model
        contents=prompt
    )

    return response.text