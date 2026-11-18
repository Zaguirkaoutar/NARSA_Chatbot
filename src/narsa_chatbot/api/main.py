from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NARSA Intelligent Chatbot API", version="0.1.0")


class ChatRequest(BaseModel):
    message: str
    language: str = "fr"


class ChatResponse(BaseModel):
    answer: str
    status: str
    language: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "narsa-chatbot"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # TODO: connecter le pipeline NLU et la base de connaissances validée.
    return ChatResponse(
        answer="Le moteur conversationnel n'est pas encore configuré.",
        status="not_configured",
        language=request.language,
    )
