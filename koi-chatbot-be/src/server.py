from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("userMessage", "")

    # Run the RAG pipeline (assuming your script processes input this way)
    result = subprocess.run(["python", "src/rag_pipeline.py", user_message], capture_output=True, text=True)
    
    return jsonify({"botResponse": result.stdout.strip()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
