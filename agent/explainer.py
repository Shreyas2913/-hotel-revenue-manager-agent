def explain_result(question, result):

    q = question.lower()

    if "cancellation rate" in q:
        return f"""
📉 Cancellation Rate: {result}%

The cancellation rate is currently healthy.

Monitor OTA channels and booking pace to avoid future revenue loss.
"""

    if "adr" in q:
        return f"""
💰 Average ADR: €{result}

ADR remains strong.

Consider protecting inventory during high-demand periods.
"""

    if "cancelled" in q:
        return f"""
❌ Cancelled Reservations: {result}

Monitor cancellation trends to reduce revenue leakage.
"""

    if "reservation" in q:
        return f"""
🏨 Total Reservations: {result}

Current booking volume looks healthy.
"""

    return str(result)