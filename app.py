# from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(
        role = "system", content="You are a poet",
    ),
    ChatMessage(role="user", content="Write a poem"),
]

# llm = Ollama(model='gemma2', temperature=0.5, context_window=2048)
llm = Ollama(model='gemma2')

response = llm.complete('Hello, how are you?')
print (response)

response = llm.chat(messages=messages)
print (response)