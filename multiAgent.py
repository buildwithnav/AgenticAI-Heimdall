import os
import asyncio
import openai

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

async def multiAgent():
    # Class that brings the model that we use; Saved the API_KEY in os.environ
    openai_model_client = OpenAIChatCompletionClient(model="gpt-4o")

    # 'agent1' and 'agent2' objects are our agents ; Assistant Agent Class from Auto-Gen; Define properties of your 'agent' like which model to use, mcp servers etc.
    #Here 'agent1' --> Maths Teacher AND 'agent2' --> Student
    agent1 = AssistantAgent(name="Maths_Teacher", model_client=openai_model_client, system_message="You are a maths teacher, make sure to explain concepts in granularity and make sure to ask students if they understood")
    agent2 = AssistantAgent(name="Student", model_client=openai_model_client, system_message="You are a student, who is smart and curious. Make sure to ask again if you did not understand a concept")

    # 'team' is an object of RoundRobinGroupChat from AutoGen, which acts like a group chat ; we will execute 'team' agent here
    # 'termination_condition' --> MaxMessageTermination
    team = RoundRobinGroupChat(participants=[agent1,agent2], termination_condition=MaxMessageTermination(max_messages=6))

    #Calling .run_stream method to execute our query ; Console -> will console the results and since used under async function we need to use await keyword
    await Console(team.run_stream(task="Lets discuss square root with examples and different cases"))
    #.close() method will terminate the session (so that token gets freed up)
    await openai_model_client.close()

asyncio.run(multiAgent())
