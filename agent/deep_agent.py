from deepagents import create_deep_agent

from langchain_openai import ChatOpenAI

from agent.config import OPENROUTER_API_KEY

from agent.deep_tools import (
    cancellation_rate,
    average_adr,
    total_reservations,
    cancelled_reservations,
    top_booking_source,
    top_guest_countries
)

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    model="deepseek/deepseek-chat-v3-0324"
)

agent = create_deep_agent(
    model=llm,
    tools=[
        cancellation_rate,
        average_adr,
        total_reservations,
        cancelled_reservations,
        top_booking_source,
        top_guest_countries
    ]
)