from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
  
)

result = model.invoke("What is the capital of France?")  # Example invocation
print(result.content)  # Output the result