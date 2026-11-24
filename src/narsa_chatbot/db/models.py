"""Modèles de persistance (conversations, messages, feedbacks)."""

from dataclasses import dataclass


@dataclass
class ConversationRecord:
    """Structure de démarrage pour une conversation persistée."""

    session_id: str
    language: str = "fr"


@dataclass
class FeedbackRecord:
    """Structure de démarrage pour un feedback utilisateur."""

    session_id: str
    rating: int
    comment: str = ""

