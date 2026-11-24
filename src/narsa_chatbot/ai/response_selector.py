"""Sélection de la meilleure réponse validée à partir de la base FAQ."""


def select_response(
    query: str,
    intent: str | None = None,
    language: str = "fr",
    faq_entries: list[dict[str, str]] | None = None,
) -> dict:
    """TODO : sélectionner une réponse validée dans la FAQ NARSA."""
    raise NotImplementedError("Implémenter la sélection de réponses.")

