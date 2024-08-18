# pip install -U llama-index llama-index-llms-ollama
from llama_index.llms.ollama import Ollama

llm = Ollama(model='llama3.1', request_timeout=30.0, context_window=2048)
response = llm.complete('Hello, who are you?')
print(response)

