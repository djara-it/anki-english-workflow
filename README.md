```
# 🇬🇧 Anki English Workflow

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-purple.svg)](https://elevenlabs.io/)
[![AnkiConnect](https://img.shields.io/badge/AnkiConnect-API-green.svg)](https://foosoft.net/projects/anki-connect/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*AI-powered English learning automation designed to eliminate repetitive friction in spaced repetition.*

</div>

---

## 🎥 Demostración en Video

> Reproducción directa del flujo automatizado de creación de tarjetas y síntesis de voz en Anki:

https://github.com/djara-it/anki-english-workflow/raw/main/anki.mp4

---

## 💡 The Problem & The Goal

> *"Learning English should take time. Managing flashcards shouldn't."*

Creating useful Anki cards manually is a repetitive burden: selecting expressions, writing translations, mapping pronunciation tags, searching for audio clips, and verifying duplicates. 

**Anki English Workflow** acts as an intelligent automation layer. Python orchestrates the pipeline, generative AI handles language understanding, and Anki remains the core spaced-repetition learning environment.

---

## ✨ Core Features

- **🤖 Intelligent Card Generation:** Transforms raw text into structured JSON data using **Google Gemini**.
- **🔊 Dual TTS with Fallback:** Native, high-quality speech generation via **ElevenLabs**, featuring automatic failover to **Gemini TTS** if quotas or connection limits are reached.
- **🛡️ Smart Duplicate Protection:** Automatically queries Anki via **AnkiConnect** to skip pre-existing entries and missing-audio updates safely.
- **⚙️ Dynamic Configuration:** Fully decoupled via `config.json` to handle custom decks, models, and customizable flashcard fields (`field_front`, `field_back`).
- **🔒 In-Memory Audio Pipeline:** Generates and transfers media bytes directly into Anki via deterministic `SHA-256` hashing (`tts_<hash>.mp3`) without polluting your local workspace with temporary files.

---

## 🏗️ Architecture & Data Flow

```text
English Input ──► Gemini AI ──► cards.json ──► Python Orchestrator
                                                        │
                      ┌─────────────────────────────────┘
                      ▼
         [ Check Existing / Missing Audio ]
                      │
           ┌──────────┴──────────┐
           ▼                     ▼
     (ElevenLabs TTS)     (Gemini TTS Fallback)
           │                     │
           └──────────┬──────────┘
                      ▼
             AnkiConnect (RAM Bytes)
                      │
                      ▼
             Anki Deck ("Inglés práctico")

```

## 📦 Project Structure

Plaintext

```
anki-english-workflow/
├── main.py             # Core automation and orchestration engine
├── gemini.py           # Google Gemini AI card generator integration
├── cards.json          # Intermediate structured card storage
├── config.json         # Flexible local preferences and field mappings
├── anki.mp4            # Demonstration screencast
├── requirements.txt    # Pinned stable Python dependencies
├── .env.example        # Template for environment variables
└── tests/              # Automated unit tests and mock integrations

```

## ⚙️ Setup & Installation

### 1. Clone the repository

Bash

```
git clone [https://github.com/djara-it/anki-english-workflow.git](https://github.com/djara-it/anki-english-workflow.git)
cd anki-english-workflow

```

### 2. Set up the Python Environment

Bash

```
python -m venv .venv
# Windows (Git Bash):
source .venv/Scripts/activate
# macOS / Linux:
source .venv/bin/activate

```

### 3. Install Dependencies

Bash

```
pip install -r requirements.txt

```

### 4. Configure AnkiConnect

1. Open **Anki Desktop**.
2. Go to **Tools → Add-ons → Get Add-ons**.
3. Paste code: `2055492159` (AnkiConnect) and restart Anki. Leave Anki open during execution.

### 5. Environment Variables (`.env`)

Create your local `.env` file from the template:

Bash

```
# Windows:
copy .env.example .env
# macOS / Linux:
cp .env.example .env

```

Open `.env` and add your secure API keys:

Fragmento de código

```
GEMINI_API_KEY="your_gemini_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"

```

### 6. Adjust `config.json`

Customize your target deck, model, and fields according to your Anki setup:

JSON

```
{
    "deck": "Inglés práctico",
    "model": "Básico",
    "field_front": "Anverso",
    "field_back": "Reverso"
}

```

## ▶️ Usage & Testing

- **Run the main workflow:**
  Bash
  ```
  python main.py

  ```
- **Run automated test suites (**`pytest`**):**
  Bash
  ```
  pytest

  ```

## 🛡️ Security & Privacy

- **Local Secrets:** API keys are restricted to your local `.env` file and are strictly ignored by Git.
- **No External DB Cloud Storage:** Keeps complete privacy by relying exclusively on Anki's local database and synchronization architecture.

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more details.

