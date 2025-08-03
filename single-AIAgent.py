import os
import asyncio
import openai

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

async def agentAI():
    # Class that brings the model that we use; Saved the API_KEY in os.environ
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # 'assistant' object is our agent ; Assistant Agent Class from Auto-Gen; Define properties of your 'assistant' like which model to use, mcp servers etc.
    assistant = AssistantAgent(name="assistant", model_client=openai_model_client)

    #Calling .run_stream method to execute our query ; Console -> will console the results and since used under async function we need to use await keyword
    await Console(assistant.run_stream(task="Explain astronomy?"))
    #.close() method will terminate the session (so that token gets freed up)
    await openai_model_client.close()

asyncio.run(agentAI())
