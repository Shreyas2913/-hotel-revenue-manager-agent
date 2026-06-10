def detect_skill(question):

    q = question.lower()

    if "cancel" in q:
        return "cancellation"

    elif "adr" in q or "revenue" in q:
        return "revenue"

    elif "source" in q or "booking" in q:
        return "booking"

    elif "lead time" in q:
        return "lead_time"

    else:
        return "general"