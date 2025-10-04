from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat_history = []
while True:
    user_input = input("Enter your query (or type 'exit' to quit): ")
    chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    response = model.invoke(chat_history)
    print("Response:", response.content)
    print()