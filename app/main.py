from agent import create_agent
from agents import Runner, set_trace_processors
import asyncio
from langsmith.wrappers import OpenAIAgentsTracingProcessor

async def main():
    agent = create_agent()
    question = input("Ask questions about a private document collection and get grounded, cited answers.\n")
    result = await Runner.run(agent, question)
    print(result.final_output)

if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())