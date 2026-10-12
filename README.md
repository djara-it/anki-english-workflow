```
# Anki English Workflow

*AI-powered English learning automation with Gemini, ElevenLabs, Python and AnkiConnect.*

<p align="center">
  <video src="anki.mp4" controls width="100%"></video>
</p>

*Anki English Workflow* is a Python-based automation project that turns useful English expressions into structured Anki flashcards and automatically adds natural AI-generated audio.

The project was created to solve a simple problem:
*Learning English should take time. Managing flashcards shouldn't.*

Instead of manually creating cards, writing translations, adding pronunciation and generating audio, the workflow automates the repetitive parts while keeping Anki as the final learning environment.

---

## ✨ What It Does

The workflow automates the creation and enrichment of English-learning cards:
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

---

## 🏗️ Architecture

```text
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

