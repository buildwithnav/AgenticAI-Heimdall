import os
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

async def agentAI():
    # Class that brings the model that we use; Saved the API_KEY in os.environ
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # Assistant Agent Class from Auto-Gen; Define properties of your 'assistant' like which model to use, mcp servers etc.
    AssistantAgent(name="assistant", model_client=openai_model_client)

asyncio.run(agentAI())
