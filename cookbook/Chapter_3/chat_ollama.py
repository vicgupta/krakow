# pip install -U llama-index llama-index-llms-ollama
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

llm = Ollama(model='llama3.1', request_timeout=30.0, context_window=2048)

messages = [
    ChatMessage(role="system", content="You are a pirate called Matey."),
    ChatMessage(role="user", content="Who are you?"),
]
response = llm.chat(messages)
print(response)