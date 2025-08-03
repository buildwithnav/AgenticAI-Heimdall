import asyncio
import os

import openai
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

async def aiAgent():

    model_client = OpenAIChatCompletionClient(model='gpt-4o')
    agent = AssistantAgent(name="Math_Teacher",
                   model_client=model_client,
                   system_message="You are maths teacher and very passionate about it." 
                   "Also when a user/student says 'DONE' you should reply back saying it was your pleasure and end session with 'GOOD LUCK'")

    human = UserProxyAgent(name="Human_Student")
    
    # 'termination_condition' --> TextMentionTermination
    team = RoundRobinGroupChat(participants=[human, agent],
                               termination_condition=TextMentionTermination("GOOD LUCK"))

    await Console((team.run_stream(task="Enter your Maths query here")))
    await model_client.close()




asyncio.run(aiAgent())