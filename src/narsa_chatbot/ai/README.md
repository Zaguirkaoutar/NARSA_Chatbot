# Module IA — NARSA AI Assistant

Responsable : **Hajar**

## Responsabilités
- Prétraitement des données textuelles (`preprocessing.py`).
- Détection de langue (réutilise `narsa_chatbot.nlp.language`).
- Classification des intentions (réutilise `narsa_chatbot.nlp.intent`).
- Extraction des entités (`entity_extractor.py`).
- Sélection des réponses à partir de la FAQ (`response_selector.py`, en lien avec `narsa_chatbot.knowledge_base`).
- Évaluation des modèles (`evaluation.py`).
- Pipeline unifié appelé par le backend (`pipeline.py`).

