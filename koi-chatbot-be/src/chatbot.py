from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
import chromadb

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Load stored vector database
embeddings = OpenAIEmbeddings()
vector_store = Chroma(collection_name="koi_website", embedding_function=embeddings, client=chroma_client)

# Define the retrieval-based QA system
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0.5),  # OpenAI GPT model
    retriever=vector_store.as_retriever(),
    return_source_documents=True
)

def chatbot_response(query):
    """
    Generates a response to user queries using retrieved KOI website data.

    Parameters:
        query (str): User's question.

    Returns:
        str: AI-generated response.
    """
    response = qa_chain({"query": query})
    return response["result"]

if __name__ == "__main__":
    while True:
        user_input = input("Ask me about KOI: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = chatbot_response(user_input)
        print("\n🤖 Chatbot: ", answer)
