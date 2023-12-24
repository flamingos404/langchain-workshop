import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI


load_dotenv()

api_key = os.getenv("OPENAI_KEY")
chat_model = ChatOpenAI(openai_api_key=api_key)

result = chat_model.predict("hi!")

print(result)
