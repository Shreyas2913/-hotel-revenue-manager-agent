from agent.skills import detect_skill

def route_question(question):

    skill = detect_skill(question)

    print(f"Using skill: {skill}")

    return skill