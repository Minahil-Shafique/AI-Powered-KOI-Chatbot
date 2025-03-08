import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load environment variables from .env file
load_dotenv()

# Get API key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("🚨 GOOGLE_API_KEY not found! Set it in the .env file.")

# Initialize embeddings with the correct model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=GOOGLE_API_KEY)

# Load KOI data
DATA_FILE = "koi_data.txt"
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(f"🚨 {DATA_FILE} not found! Run the scraper first.")

loader = TextLoader(DATA_FILE)
documents = loader.load()

# Chunk text for embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Store in ChromaDB
vector_db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
vector_db.persist()

print("✅ Data successfully stored in ChromaDB!")
