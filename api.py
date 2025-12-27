from fastapi import FastAPI
from pydantic import BaseModel
from llm_agent import answer_with_llm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # <-- MUST COME FIRST

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    with open("api_docs/auth_api.md", "r", encoding="utf-8") as f:
        context = f.read()

    answer = answer_with_llm(q.question, context)
    return {"answer": answer}
