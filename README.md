# Anki English Workflow

> **AI-powered English learning automation with Gemini, ElevenLabs, Python and AnkiConnect.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-black)](https://elevenlabs.io/)
[![AnkiConnect](https://img.shields.io/badge/AnkiConnect-API-2E7D32)](https://foosoft.net/projects/anki-connect/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Anki English Workflow** is a Python-based automation project that turns useful English expressions into structured Anki flashcards and automatically adds natural AI-generated audio.

The project was created to solve a simple problem:

> **Learning English should take time. Managing flashcards shouldn't.**

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

---

## 🎯 Why I Built This

This project started from a practical need: **make English learning more efficient through automation**.

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

The goal of this project is therefore not to replace learning, but to **remove unnecessary friction from the learning process**.

The learner focuses on learning English.

The workflow handles the repetitive work.

---

# 🏗️ Architecture

The project follows a simple pipeline architecture where each component has a specific responsibility.

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
                    │    data     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Python    │
                    │ Orchestrator │
                    └──────┬───────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          Existing card?       Missing audio?
                 │                   │
                 │                   ▼
                 │            ┌──────────────┐
                 │            │ ElevenLabs   │
                 │            │     TTS      │
                 │            └──────┬───────┘
                 │                   │
                 │              If failure
                 │                   │
                 │                   ▼
                 │            ┌──────────────┐
                 │            │ Gemini TTS   │
                 │            │   Fallback   │
                 │            └──────┬───────┘
                 │                   │
                 └─────────┬─────────┘
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

---

# 🧩 Technologies

| Technology | Role |
|---|---|
| **Python** | Main workflow orchestrator |
| **Google Gemini** | Generates structured English-learning cards |
| **ElevenLabs** | Primary text-to-speech provider |
| **Gemini TTS** | Automatic audio fallback |
| **AnkiConnect** | API bridge between Python and Anki |
| **JSON** | Simple intermediate data format |
| **Anki** | Final spaced-repetition learning environment |

---

# 🧠 Design Decisions

The project was intentionally designed around simple, replaceable components rather than tightly coupling everything together.

## Python as the Orchestrator

Python was chosen as the central layer because it provides a simple way to:

- communicate with APIs;
- process JSON;
- handle errors;
- manage the workflow;
- communicate with AnkiConnect;
- integrate multiple AI services.

Python acts as the **glue between the different systems** rather than trying to perform every task itself.

---

## Google Gemini for Card Generation

Gemini is responsible for transforming raw learning content into structured flashcards.

The generated information follows a predictable schema:

```json
{
  "front": "I need to reschedule.",
  "back": "Necesito cambiar la fecha.",
  "pronunciation": "Ai nid tu rischediul.",
  "tags": [
    "english",
    "daily"
  ]
}
```

This separation makes the AI responsible for **language understanding**, while Python remains responsible for **automation and execution**.

---

## ElevenLabs as the Primary TTS Provider

ElevenLabs was selected as the primary text-to-speech provider because natural pronunciation is particularly important for a language-learning application.

The goal is not simply to produce understandable audio, but to expose the learner to more natural spoken English.

---

## Gemini TTS as a Fallback

The workflow does not depend exclusively on one TTS provider.

If ElevenLabs fails or is unavailable, the system automatically attempts to generate the audio using Gemini TTS.

```text
ElevenLabs
     │
     ├── Success ───────► Continue
     │
     └── Failure
            │
            ▼
        Gemini TTS
            │
            ├── Success ─► Continue
            │
            └── Failure ─► Report error
```

This makes the audio generation process more resilient.

---

## AnkiConnect Instead of Building a Flashcard System

Anki already provides a mature spaced-repetition system.

Instead of reinventing:

- card scheduling;
- reviews;
- synchronization;
- deck management;
- learning algorithms;

the project uses **AnkiConnect** as an API bridge.

This keeps the project focused on what it actually adds:

> **Automating the creation and enrichment of learning material.**

---

## `cards.json` as an Intermediate Interface

`cards.json` provides a simple boundary between content generation and the automation layer.

This has several advantages:

- human-readable;
- easy to inspect;
- easy to edit;
- easy to version with Git;
- independent from Anki;
- easy to replace with another data source in the future.

The project therefore does not require the AI layer and Anki integration to be directly coupled.

---

# 🔊 Audio Architecture

Generated audio is handled entirely in memory before being sent to Anki.

```text
ElevenLabs
     │
     ▼
 Audio bytes in RAM
     │
     ▼
 AnkiConnect
     │
     ▼
 Anki media collection
```

The workflow does **not** need to create temporary MP3 or WAV files inside the project directory.

This keeps the repository clean and avoids unnecessary intermediate files.

Anki itself still stores the audio in its own `collection.media` directory, which is expected because the media must be available to Anki.

---
# ☁️ Why No Cloud Storage?

The workflow intentionally avoids using an additional cloud storage layer for cards or generated audio.

This is a deliberate architectural decision, not a missing component.

```text
Gemini / ElevenLabs
        ↓
      Python
        ↓
   AnkiConnect
        ↓
       Anki
        ↓
      AnkiWeb
```

Anki already provides the storage and synchronization layer required by the learning workflow. Adding services such as Google Drive, Amazon S3 or Firebase would introduce additional infrastructure without providing enough value for the current scope.

### Why?

- **Less complexity** — no additional storage service or backend needs to be maintained.
- **Lower cost** — no additional cloud storage is required for generated audio.
- **Fewer failure points** — every extra service introduces another dependency.
- **Better privacy** — learning content does not need to be stored in an additional third-party service.
- **Cleaner architecture** — Python orchestrates the workflow while Anki manages the final learning data.
- **Efficient audio handling** — generated audio is kept in memory and sent directly to AnkiConnect instead of being unnecessarily stored as temporary project files.

The audio flow is therefore:

```text
ElevenLabs
     ↓
Audio bytes in memory
     ↓
AnkiConnect
     ↓
Anki collection.media
     ↓
AnkiWeb synchronization
```

Cloud infrastructure may become useful in a future version if the project evolves into a web application, requires centralized storage, scheduled server-side processing, or supports multiple users.

For the current project, however, **avoiding unnecessary infrastructure keeps the system simpler, cheaper and easier to maintain.**

# 🛡️ Duplicate Protection

Automation should be safe to run repeatedly.

The workflow therefore checks whether a card already exists before creating it.

The search is performed using the `Anverso` field:

```text
Anverso:"English sentence"
```

This prevents the same English expression from being repeatedly inserted into the deck.

Audio generation also has its own protection.

If the note already contains:

```text
[sound:...]
```

the workflow does not generate another audio file.

---

# 🔑 Deterministic Audio Names

Audio filenames are generated using a SHA-256 hash derived from the English sentence.

Conceptually:

```text
English sentence
       │
       ▼
    SHA-256
       │
       ▼
 deterministic filename
```

For example:

```text
tts_<hash>.mp3
```

This gives the same expression a predictable media filename and reduces the possibility of naming collisions.

---

# 📦 Project Structure

```text
anki-english-workflow/
│
├── main.py
├── gemini.py
├── cards.json
├── config.json
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

Your real keys live in a local `.env` file. That file is not in Git and should never be uploaded.

### Main components

**`main.py`**

The main automation engine.

Responsible for:

- loading configuration;
- reading cards;
- communicating with AnkiConnect;
- detecting existing notes;
- creating missing cards;
- generating audio;
- attaching audio to notes;
- reporting results.

**`gemini.py`**

Handles AI-powered card generation using the Gemini API.

**`cards.json`**

Stores the structured English-learning cards.

**`config.json`**

Contains local configuration used by the workflow.

**`tests/`**

Contains focused tests for the project's main integrations and behavior.

---

# 📝 Card Format

Cards use a deliberately simple JSON structure:

```json
[
  {
    "front": "I need to reschedule.",
    "back": "Necesito cambiar la fecha.",
    "pronunciation": "Ai nid tu rischediul.",
    "tags": [
      "english",
      "daily"
    ]
  }
]
```

The format is intentionally kept independent from Anki's internal representation.

Python handles the conversion between this simple structure and the Anki note model.

---

# ⚙️ How It Works

The workflow can be summarized in eight steps:

### 1. Load the cards

Python reads `cards.json`.

### 2. Load configuration

The application loads `config.json` and reads API keys from your local `.env` file.

### 3. Check Anki

Each English expression is searched in the Anki deck.

### 4. Prevent duplicates

Existing cards are skipped instead of being recreated.

### 5. Generate missing audio

Cards without audio receive AI-generated speech.

ElevenLabs is attempted first, followed by Gemini TTS if necessary.

### 6. Store audio

Audio is sent directly to AnkiConnect without creating temporary project files.

### 7. Attach audio to the card

The note is updated with the corresponding Anki `[sound:...]` reference.

### 8. Report the result

The workflow provides a summary:

```text
Creadas: 0
Ya existentes: 30
Audios añadidos: 0
Errores: 0
```

This makes repeated execution safe and easy to monitor.

---

# 🚀 Installation

## What you need

- Python 3
- [Anki Desktop](https://apps.ankiweb.net/)
- A [Google Gemini](https://aistudio.google.com/apikey) API key
- An [ElevenLabs](https://elevenlabs.io/) API key

## 1. Download the project

```bash
git clone https://github.com/djara-it/anki-english-workflow.git
cd anki-english-workflow
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

## 3. Turn it on

Windows:

```cmd
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

## 4. Install the packages

```bash
pip install -r requirements.txt
```

## 5. Connect Anki

1. Open Anki.
2. Go to **Tools → Add-ons → Get Add-ons**.
3. Paste this code and install it: `2055492159` (AnkiConnect).
4. Restart Anki and leave it open.

## 6. Add your API keys

The project reads secrets from a local `.env` file. That file stays on your computer.

**Step 1 — Copy the example file**

Windows:

```cmd
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

**Step 2 — Open `.env` and paste your keys**

```env
GEMINI_API_KEY="your_gemini_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_key_here"
```

Replace the placeholder text with your real keys. Save the file.

Do not share `.env` and do not commit it to Git. `.env.example` is only a template and has no secrets.

---

# ▶️ Usage

Keep Anki open, then run:

```bash
python main.py
```

On Windows you can also run:

```cmd
.venv\Scripts\python.exe main.py
```

The workflow will process the cards and report what happened.

Example:

```text
Resumen:
Creadas: 2
Ya existentes: 28
Audios añadidos: 3
Errores: 0
```

Running the workflow again should not recreate cards or audio that already exist.

---

# 🔄 Why This Workflow Is Useful

The project is useful because it combines several repetitive tasks into a single automated process.

Instead of:

```text
Find phrase
   ↓
Translate
   ↓
Write pronunciation
   ↓
Generate audio
   ↓
Create Anki card
   ↓
Check duplicates
   ↓
Repeat
```

the workflow reduces the process to:

```text
Provide useful learning content
            ↓
       Run workflow
            ↓
       Study in Anki
```

The automation therefore acts as a **productivity layer around Anki**, rather than replacing Anki itself.

---

# 🔮 Future Improvements

Possible future directions include:

- automatic ingestion of English lessons or conversations;
- more advanced card selection;
- automatic filtering of low-value or duplicate expressions;
- additional TTS providers;
- a lightweight web interface;
- richer learning statistics;
- scheduled automation;
- optional n8n integration;
- additional language support.

These are potential extensions rather than current features.

---

# 🧪 Testing

The project includes focused tests for important components such as:

- card retrieval;
- audio generation;
- ElevenLabs integration;
- card generation.

The goal is to test individual integrations without requiring the entire workflow to run every time.

---

# 🧭 Why Not n8n?

n8n was considered as a possible orchestration layer.

For the current scope, Python was preferred because the workflow is relatively compact and requires direct control over:

- API responses;
- JSON processing;
- AnkiConnect;
- audio bytes;
- duplicate detection;
- error handling.

Introducing a visual workflow engine at this stage would add another dependency without providing enough benefit.

However, n8n could become useful in a future version if the workflow expands to include scheduled jobs, multiple external sources or more complex automation.

---

# 🔐 Security

API keys never belong in `main.py`, `gemini.py`, or GitHub.

How this project keeps them safe:

1. Copy `.env.example` to `.env`.
2. Put your Gemini and ElevenLabs keys only in `.env`.
3. Git ignores `.env`, so it is not uploaded.

Also ignored: the virtual environment, Python cache files, and generated audio files.

---

# 📚 What This Project Demonstrates

Although the project was created for English learning, it also demonstrates several practical software-engineering concepts:

- Python automation
- REST/API integration
- Generative AI integration
- Text-to-speech integration
- JSON data modeling
- API fallback strategies
- Error handling
- Duplicate prevention
- Deterministic resource naming
- In-memory binary data processing
- External application integration
- Automated testing
- Git/GitHub workflow

The project is therefore both a **personal productivity tool** and a practical example of integrating multiple modern APIs into a real-world automation pipeline.

---

# 👨‍💻 Project Philosophy

The main idea behind this project is simple:

> **Use technology to remove repetitive work, not to add unnecessary complexity.**

Anki is already excellent at helping people learn.

Gemini is excellent at understanding and generating language.

ElevenLabs is excellent at producing natural speech.

Python is excellent at connecting systems together.

AnkiConnect provides the bridge between automation and Anki.

Instead of rebuilding these tools, this project connects them into a single practical workflow.

---

## ⭐ If you find this project useful

Feel free to explore the repository, experiment with the workflow, or adapt the architecture to your own learning system.

**Built with Python, AI and a practical goal: spend less time managing flashcards and more time learning.**