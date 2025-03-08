import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("🚨 GOOGLE_API_KEY not found! Set it in the .env file.")

# Load vector database with embeddings
vector_db = Chroma(persist_directory="./chroma_db")

# Load Gemini-Pro Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

def generate_answer(prompt):
    return llm.invoke([HumanMessage(content=prompt)])  # Use invoke() instead of predict()

# Example Usage
if __name__ == "__main__":
    question = "What courses does KOI offer?"
    response = generate_answer(question)
    print(response.content)
