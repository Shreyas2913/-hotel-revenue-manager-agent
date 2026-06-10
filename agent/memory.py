conversation_memory = []

def save_memory(question):
    conversation_memory.append(question)

def get_memory():
    return conversation_memory[-5:]