# pip install -U llama-index llama-index-llms-openai
import os
from llama_index.llms.openai import OpenAI

llm = OpenAI(model='gpt-3.5-turbo', api_key=os.environ['OPENAI_API_KEY'])
response = llm.complete('Hello, who are you?')
print(response)
