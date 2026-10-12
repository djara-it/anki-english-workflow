```
# Anki English Workflow

*AI-powered English learning automation with Gemini, ElevenLabs, Python and AnkiConnect.*

<!-- Demostración en video del flujo completo -->
<video src="anki.mp4" autoplay loop muted playsinline width="100%"></video>

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-purple.svg)](https://elevenlabs.io/)
[![AnkiConnect](https://img.shields.io/badge/AnkiConnect-API-green.svg)](https://foosoft.net/projects/anki-connect/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Anki English Workflow* is a Python-based automation project that turns useful English expressions into structured Anki flashcards and automatically adds natural AI-generated audio.

The project was created to solve a simple problem:
*Learning English should take time. Managing flashcards shouldn't.*

Instead of manually creating cards, writing translations, adding pronunciation and generating audio, the workflow automates the repetitive parts while keeping Anki as the final learning environment.

---

## ✨ What It Does

The workflow automates the creation and enrichment of English-learning cards.
It can:
- Generate useful English expressions with **Google Gemini**
- Provide natural Spanish translations
- Generate pronunciation approximations
- Generate English audio with **ElevenLabs**
- Use **Gemini TTS as an automatic fallback**
- Send cards and audio directly to **Anki**
- Detect existing cards and avoid duplicates
- Detect cards that already contain audio
- Store generated audio directly in Anki without creating temporary audio files in the project
- Keep the card data in a simple, reusable JSON format

The result is a much more efficient learning workflow:
```text
English content
      │
      ▼
   Gemini AI
      │
      ▼
Useful English expressions
      │
      ├── Spanish translation
      ├── Pronunciation
      └── Tags
      │
      ▼
   Python Workflow
      │
      ├── Check existing cards
      ├── Generate missing audio
      └── Prevent duplicates
      │
      ▼
  ElevenLabs TTS
      │
      └── Gemini TTS fallback
      │
      ▼
   AnkiConnect
      │
      ▼
 Anki — "Inglés práctico"

```

## 🎯 Why I Built This

This project started from a practical need: *make English learning more efficient through automation*.

Creating a useful Anki card manually involves several repetitive steps:

1. Choose a useful English expression.
2. Write the Spanish translation.
3. Add a pronunciation approximation.
4. Add appropriate tags.
5. Generate or find audio.
6. Import the card into Anki.
7. Make sure it doesn't already exist.
8. Repeat everything for the next expression.

Doing this occasionally is fine. Doing it consistently becomes tedious.

The goal of this project is therefore not to replace learning, but to *remove unnecessary friction from the learning process*.

The learner focuses on learning English.

The workflow handles the repetitive work.

## 🏗️ Architecture

The project follows a simple pipeline architecture where each component has a specific responsibility.

Plaintext

```
┌──────────────┐
│   English    │
│    Input     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Gemini    │
│     AI       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  cards.json  │
│ Structured   │
│    data      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Python    │
│ Orchestrator │
└──────┬───────┘
       │
 ┌─────┴─────┐
 │           │
 ▼           ▼
Existing card? Missing audio?
 │           │
 │           ▼
 │    ┌──────────────┐
 │    │ ElevenLabs   │
 │    │     TTS      │
 │    └──────┬───────┘
 │           │
 │      If failure
 │           │
 │           ▼
 │    ┌──────────────┐
 │    │ Gemini TTS   │
 │    │   Fallback   │
 │    └──────┬───────┘
 │           │
 └─────┬─────┘
       ▼
┌──────────────┐
│ AnkiConnect  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     Anki     │
│     Deck     │
└──────────────┘

```

## 🧩 Technologies


|                   |                                              |
| ----------------- | -------------------------------------------- |
| **Technology**    | **Role**                                     |
| **Python**        | Main workflow orchestrator                   |
| **Google Gemini** | Generates structured English-learning cards  |
| **ElevenLabs**    | Primary text-to-speech provider              |
| **Gemini TTS**    | Automatic audio fallback                     |
| **AnkiConnect**   | API bridge between Python and Anki           |
| **JSON**          | Simple intermediate data format              |
| **Anki**          | Final spaced-repetition learning environment |


## 🧠 Design Decisions

The project was intentionally designed around simple, replaceable components rather than tightly coupling everything together.

### Python as the Orchestrator

Python was chosen as the central layer because it provides a simple way to:

- communicate with APIs;
- process JSON;
- handle errors;
- manage the workflow;
- communicate with AnkiConnect;
- integrate multiple AI services.

### Google Gemini for Card Generation

Gemini is responsible for transforming raw learning content into structured flashcards:

JSON

```
{
  "front": "I need to reschedule.",
  "back": "Necesito cambiar la fecha.",
  "pronunciation": "Ai nid tu rischediul.",
  "tags": ["english", "daily"]
}

```

### ElevenLabs & Gemini TTS Fallback

ElevenLabs provides natural pronunciation as the primary TTS provider. If it fails, the system automatically falls back to Gemini TTS.

## 📦 Project Structure

Plaintext

```
anki-english-workflow/
│
├── main.py
├── gemini.py
├── cards.json
├── config.json
├── anki.mp4
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── tests/
    ├── buscar_tarjeta_sin_audio.py
    ├── test_audio_una_tarjeta.py
    ├── test_elevenlabs.py
    └── test_generate.py

```

## 🚀 Installation & Quick Start

### 1. Download the project

Bash

```
git clone [https://github.com/djara-it/anki-english-workflow.git](https://github.com/djara-it/anki-english-workflow.git)
cd anki-english-workflow

```

### 2. Set up your environment

Bash

```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt

```

### 3. Configure AnkiConnect

1. Open **Anki Desktop**.
2. Go to *Tools → Add-ons → Get Add-ons*.
3. Paste code: `2055492159` and restart Anki.

### 4. Add your API Keys

Bash

```
# Windows:
copy .env.example .env
# macOS / Linux:
cp .env.example .env

```

Open `.env` and fill in your keys:

Fragmento de código

```
GEMINI_API_KEY="your_gemini_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_key_here"

```

## ▶️ Usage

Keep Anki open, then run:

Bash

```
python main.py

```

## 🧪 Testing

Bash

```
pytest

```

## 📚 License

This project is open-source under the MIT License.

```

```

