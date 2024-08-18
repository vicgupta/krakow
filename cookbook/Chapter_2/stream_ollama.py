# pip install -U llama-index llama-index-llms-ollama
from llama_index.llms.ollama import Ollama

llm = Ollama(model='llama3.1', request_timeout=30.0, context_window=2048)

stream_response = llm.stream_complete("Write a detailed essay on the impact of AI on the future of work.")

for t in stream_response:
    print(t.delta, end="")
