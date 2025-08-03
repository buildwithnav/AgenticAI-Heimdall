import asyncio
import json
import os

import openai
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

async def agentAI():
    model_client = OpenAIChatCompletionClient(model='gpt-4o')
    agent1 = AssistantAgent(name="agent1",
                            model_client=model_client )
    agent2 = AssistantAgent(name="agent2",
                            model_client=model_client)

    await Console(agent1.run_stream(task="My favorite color is blue."))

    #Saving state of agent1 asynchronously
    state = await agent1.save_state()
    #Creating a file with write mode and saving our state there
    with open("memory.json", "w") as f:
        json.dump(state, f)

    #Opening that file and load the state into a variable called 'saved_state'
    with open("memory.json", "r") as f:
        saved_state = json.load(f)

    #loading the saved state onto agent2
    await agent2.load_state(saved_state)
    await Console(agent2.run_stream(task="What is my favorite color?."))
    await model_client.close()


asyncio.run(agentAI())