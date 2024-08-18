from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama

llm = Ollama(model='llama3.1', request_timeout=30.0, context_window=2048)

documents = SimpleDirectoryReader(".").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is second amendment?")
print(response)