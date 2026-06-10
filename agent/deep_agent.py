from deepagents import create_deep_agent

from agent.semantic_tools import (
    get_cancellation_rate,
    get_average_adr,
    get_total_reservations,
    get_cancelled_reservations,
    get_top_booking_source,
    get_top_guest_countries
)

agent = create_deep_agent(
    tools=[
        get_cancellation_rate,
        get_average_adr,
        get_total_reservations,
        get_cancelled_reservations,
        get_top_booking_source,
        get_top_guest_countries
    ]
)