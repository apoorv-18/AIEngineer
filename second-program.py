from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()
response = client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = [{
        "role": "user",
        "content": "tell me today's current date"
    }]
)

print(response.choices[0].message.content)
