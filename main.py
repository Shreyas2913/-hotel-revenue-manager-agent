from agent.agent import generate_sql
from agent.tools import run_sql
from agent.router import route_question
from agent.memory import save_memory, get_memory

print("Hotel Revenue Manager Agent")
print("Type exit to quit")

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    try:

        # Save question to memory
        save_memory(question)

        # Route question to a skill
        skill = route_question(question)

        print(f"\nSelected Skill: {skill}")

        # Generate SQL
        sql = generate_sql(question)

        print("\nGenerated SQL:")
        print(sql)

        # Run SQL
        result = run_sql(sql)

        print("\nAnswer:")

        if len(result) == 1 and len(result[0]) == 1:
            print(result[0][0])
        else:
            for row in result:
                print(row)

        print("\nRecent Memory:")
        print(get_memory())

    except Exception as e:
        print("\nError:")
        print(e)