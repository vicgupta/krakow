# pip install -U llama-index llama-index-llms-groq
import os
from llama_index.llms.groq import Groq
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv
load_dotenv()

llm = Groq(model='llama3-70b-8192', request_timeout=30.0, context_window=2048, api_key=os.environ['GROQ_API_KEY'])

messages = [
    ChatMessage(role="system", content="You are a pirate called Matey."),
    ChatMessage(role="user", content="Who are you?"),
]
response = llm.chat(messages)
print(response)