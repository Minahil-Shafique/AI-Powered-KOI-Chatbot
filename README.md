# AI-Powered KOI Chatbot

This project is an AI-driven chatbot utilizing a **Retrieval-Augmented Generation (RAG) pipeline** to process and retrieve information from the **KOI website**. It is built using **Python, LangChain, ChromaDB, and Google Gemini AI**, with seamless integration for efficient data retrieval.

## 🚀 Features
- **Data Loading & Processing**: Extracts and splits KOI website content into manageable chunks.
- **Vector Embeddings**: Generates vector embeddings using `GoogleGenerativeAIEmbeddings`.
- **Vector Database**: Stores embeddings in **ChromaDB** for quick retrieval.
- **LLM-based Response Generation**: Uses **Gemini-Pro** to generate intelligent responses based on retrieved content.

---

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/koi-chatbot.git
cd koi-chatbot
```
###2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
###4️⃣ Set Up Environment Variables
```bash
GOOGLE_API_KEY=your_google_api_key
```

---
## 📌 Steps to Run the Project
### ✅ **Step 1: Load & Store Data**
```bash
python process_data.py
```

### ✅ **Step 2: Run the Chatbot API**
```bash
python chatbot.py
```

### ✅ **Step 4: Run the Frontend**
```bash
cd frontend
npm install
npm run dev
```
- Launches the chatbot UI.

---

## ⚡ Technologies Used
- **Backend**:Python, LangChain, Google AI (Gemini-Pro), ChromaDB
- **Frontend**: Next.js (React), Tailwind CSS
- **Data Processing**: BeautifulSoup, Google AI Embeddings
