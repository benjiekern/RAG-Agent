from agent import create_agent
from agents import Agent, Runner, function_tool, set_trace_processors
import asyncio
from dotenv import load_dotenv, find_dotenv
from langsmith.wrappers import OpenAIAgentsTracingProcessor

async def main():
    agent = create_agent()
    question = "What is the weather in Berlin?"
    result = await Runner.run(agent, question)
    print(result.final_output)

if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())