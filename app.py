# from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.llms.ollama import 

messages = [
    ChatMessage(
        role = "system", content="You are a poet",
    ),
    ChatMessage(role="user", content="Write a poem"),
]

# Create an Ollama LLM
# llm = Ollama(model='gemma2', temperature=0.5, context_window=2048)
llm = Ollama(model='gemma2')
# Create an agent
# agent = ReActAgent(llm=llm,verbose=True)

response = llm.complete('Hello, how are you?')
print (response)
# agent.respond('Hello, how are you?')

# response = llm.stream_complete('Hello, how are you?')
# for r in response:
#     print (r.delta, end="")

response = llm.chat(messages=messages)
print (response)