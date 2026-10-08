from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

response = model.invoke("Who is Virat Kohli?")

print(response.content)