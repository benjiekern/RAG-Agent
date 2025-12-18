from agents import Agent, Runner, function_tool, set_trace_processors
import asyncio
from dotenv import load_dotenv, find_dotenv
from langsmith.wrappers import OpenAIAgentsTracingProcessor
import os
import requests


load_dotenv(find_dotenv())
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@function_tool
def get_weather(city: str) -> str:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={"key": WEATHER_API_KEY, "q": city}
    )
    data = response.json()

    if "error" in data:
        return f"Weather API error: {data['error']['message']}"

    return f"{data['current']['temp_f']}°F, {data['current']['condition']['text']}"


def create_agent():
    return Agent(
        name="Weather Agent",
        instructions="You are sarcastic, rude, and will only respond in German.",
        tools=[get_weather],
    )