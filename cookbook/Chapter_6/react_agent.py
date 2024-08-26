from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool

def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)
def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)

messages = [
    ChatMessage(
        role = "system", content="You are a poet",
    ),
    ChatMessage(role="user", content="Write a poem"),
]

# llm = Ollama(model='gemma2', temperature=0.5, context_window=2048)
llm = Ollama(model='gemma2')

# Create an agent
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
response = agent.chat("What is 20+(2*4)? Calculate step by step ")
print(response)


