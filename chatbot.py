from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
)

syetem_message = SystemMessage(
    content="You are a helpful AI assistant."
)
chat_history = []
chat_history.append(syetem_message)

while True:
    user_input = input("Enter your mesage (or 'exit' to quit): ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break

    result = model.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))
    print(result.content)  