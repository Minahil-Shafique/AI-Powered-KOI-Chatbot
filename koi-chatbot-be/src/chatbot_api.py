from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from rag_pipeline import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chat")
async def chat(query: Query):
    response = generate_answer(query.question)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
