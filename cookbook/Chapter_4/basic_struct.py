# pip install -U llama-index llama-index-llms-ollama
# As Ollama does not support structured input, we will use OpenAI for this example.
import os
from llama_index.llms.openai import OpenAI
from llama_index.core.bridge.pydantic import BaseModel
from llama_index.core.llms import ChatMessage

class Song(BaseModel):
    """A song with name and artist."""
    name: str
    artist: str

llm = OpenAI(model='gpt-3.5-turbo', api_key=os.environ['OPENAI_API_KEY'])

sllm = llm.as_structured_llm(Song)
response = sllm.chat([ChatMessage(role="user", content="Name another random song!")])
print(response.message.content)