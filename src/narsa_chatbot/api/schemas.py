"""Schémas Pydantic partagés pour l'API FastAPI."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    language: str = "fr"


class ChatResponse(BaseModel):
    answer: str
    status: str
    language: str


class FeedbackRequest(BaseModel):
    session_id: str
    rating: int = Field(ge=1, le=5)
    comment: str = ""

