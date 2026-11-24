"""Prétraitement et normalisation des textes multilingues (FR, AR, Darija)."""


def preprocess_text(text: str) -> str:
    """Nettoie et normalise un message utilisateur avant analyse."""
    return text.strip()

