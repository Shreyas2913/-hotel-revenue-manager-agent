from langchain.tools import tool

from agent.semantic_tools import (
    get_cancellation_rate,
    get_average_adr,
    get_total_reservations,
    get_cancelled_reservations,
    get_top_booking_source,
    get_top_guest_countries
)


@tool
def cancellation_rate():
    """Get hotel cancellation rate percentage."""
    return str(get_cancellation_rate())


@tool
def average_adr():
    """Get average ADR for reserved bookings."""
    return str(get_average_adr())


@tool
def total_reservations():
    """Get total reservations."""
    return str(get_total_reservations())


@tool
def cancelled_reservations():
    """Get total cancelled reservations."""
    return str(get_cancelled_reservations())


@tool
def top_booking_source():
    """Get booking source with highest reservations."""
    return str(get_top_booking_source())


@tool
def top_guest_countries():
    """Get top guest countries."""
    return str(get_top_guest_countries())