<<<<<<< HEAD
# NARSA Intelligent Chatbot

Squelette de projet inspiré de Cookiecutter Data Science et adapté au CPS N°29/NARSA/2026.

## Fonctionnalités ciblées selon le CPS
- Base de connaissances et FAQ questions/réponses.
- NLP/NLU et détection des intentions.
- Français, arabe classique et darija marocaine (amazighe en option).
- Interaction texte/voix : STT et TTS.
- Supervision, administration, satisfaction et analytics.
- Analyse des sentiments et transfert éventuel vers un agent humain.
- Sécurité et protection des données personnelles.

## Installation sous Windows (VS Code)
```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
uvicorn narsa_chatbot.api.main:app --reload
```
Puis ouvrir http://127.0.0.1:8000/docs

## Dossiers
- `data/`: données brutes, intermédiaires et préparées.
- `notebooks/`: exploration et expérimentations.
- `src/narsa_chatbot/`: code Python organisé par modules.
- `models/`: modèles entraînés.
- `tests/`: tests automatisés.
- `docs/`: cadrage, architecture, sécurité et tests.
- `reports/`: résultats et analyses.

**Important :** ce dossier est un squelette de démarrage, pas un chatbot terminé. Les réponses doivent être vérifiées à partir de sources officielles NARSA. Ne pas ajouter de données personnelles réelles. Les intégrations, modèles NLP, STT/TTS et mécanismes de sécurité restent à développer et valider.
=======
# NARSA_Chatbot
>>>>>>> a5b549d59161981e9eaf6066e6ca50b816e40a76
