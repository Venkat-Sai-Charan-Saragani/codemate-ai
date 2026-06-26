import os
from dotenv import load_dotenv
from openai import OpenAI

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_response(messages):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            *messages
        ],
        temperature=0.4,
        max_tokens=2048,
    )
    return response.choices[0].message.content