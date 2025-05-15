from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

## create char prompt template with message placeholders
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{user_query}')
])

chat_history = []
user_query = "Where is my refund?"

# load chat hotory from a file
def load_chat_history(file_path):
    with open(file_path, 'r') as file:
        chat_history.extend(file.readlines())

load_chat_history('chat_history.txt')

print(chat_history)

#create prompt with message placeholders
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "user_query": user_query
})

print(prompt)