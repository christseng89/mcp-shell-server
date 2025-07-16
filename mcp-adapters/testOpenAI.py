import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key, timeout=60)

# Make a simple chat completion request
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(completion.choices[0].message.content)
