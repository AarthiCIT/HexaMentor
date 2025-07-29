from ollama import Client
client = Client(host='http://localhost:11434')

def generate_question(topic, difficulty):
    prompt = f"Generate one MCQ on the topic '{topic}' with difficulty level '{difficulty}'. Provide 4 options and indicate the correct answer."
    response = client.chat(model='phi3:mini', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']