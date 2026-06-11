from agent.deep_agent import agent
from agent.agent import generate_sql
from agent.tools import run_sql


def ask_agent(question):

    q = question.lower()

    # Force SQL for analytical questions
    if (
        "compare" in q
        or "highest" in q
        or "lowest" in q
        or "trend" in q
        or "which country" in q
        or "which source" in q
        or "percentage" in q
        or "most" in q
    ):

        try:

            sql = generate_sql(question)
            result = run_sql(sql)

            if len(result) == 1 and len(result[0]) == 1:
                return str(result[0][0])

            if "compare" in q:
                return f"📊 Comparison Result\n\n{result}"

            return str(result)

        except Exception:
            pass

    # Try Deep Agent first
    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        if answer and len(answer.strip()) > 5:
            return answer

    except Exception:
        pass

    # Final SQL fallback
    try:

        sql = generate_sql(question)
        result = run_sql(sql)

        if len(result) == 1 and len(result[0]) == 1:
            return str(result[0][0])

        return str(result)

    except Exception as e:

        return f"Unable to answer question: {e}"