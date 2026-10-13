# Anki English Workflow

**Turn useful English expressions into Anki flashcards with natural AI-generated audio.**

A personal project that combines programming and language learning to automate the repetitive part of flashcard creation, while Anki stays the place where you study.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white) ![ElevenLabs](https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logo=elevenlabs&logoColor=white) ![AnkiConnect](https://img.shields.io/badge/AnkiConnect-2D8CFF?style=for-the-badge) ![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)[

---

## 🎬 Project Demo

[https://github.com/user-attachments/assets/10d77069-8d28-48fe-9d52-d90dcf9a6bb9](https://github.com/user-attachments/assets/10d77069-8d28-48fe-9d52-d90dcf9a6bb9)

## 📌 About the Project

Creating a good flashcard by hand means writing the translation, adding audio, importing it and checking for duplicates. **Anki English Workflow** automates that repetitive part. It reads your expressions from a JSON file, talks to a local Anki installation through AnkiConnect, and attaches natural audio to every card.

## ✨ What it does today

- 🗂️ Reads English expressions from `cards.json` (front, Spanish translation, pronunciation hint, tags).
- 🔄 Looks each expression up in Anki and **skips cards that already exist**.
- 🔊 Generates audio with **ElevenLabs** and falls back to **Gemini TTS** if that fails.
- 💾 Stores the audio directly in Anki (no audio files are written to the project folder).
- ♻️ Is safe to run repeatedly: existing cards and cards that already have audio are not touched.
- 🛑 Stops cleanly if Anki is closed or AnkiConnect fails, without spending audio credit.
- 🤖 Optionally generates card JSON from a text file with **Gemini**, saved to a separate file so you can review it before importing.
- 📊 Prints a summary: created cards, existing cards, audios added, errors.

## 🚧 What it does not do (yet)

- No automated unit tests (see [Testing](https://claude.ai/chat/31d8b5e5-d42e-4285-a96f-380db492f687#-testing)).
- Generated cards are not imported automatically. You review them first, on purpose, because the pronunciation hint is an AI approximation.
- One deck and one note type, set in `config.json`.

## 🛠️ Tech Stack


| Technology    | Purpose                                     |
| ------------- | ------------------------------------------- |
| Python        | Application logic and automation            |
| AnkiConnect   | Communication with Anki Desktop             |
| ElevenLabs    | Text-to-speech (primary)                    |
| Google Gemini | Text-to-speech fallback and card generation |
| JSON          | Flashcard data and configuration            |


## 🔄 How It Works

```text
cards.json ──► main.py ──► for each card:
                             ├─ find it in Anki (AnkiConnect)
                             ├─ already exists with audio? skip
                             ├─ generate audio: ElevenLabs ─► (on failure) Gemini TTS
                             ├─ store audio in Anki media
                             └─ create the note or attach the audio to the existing one

Optional:  texto.txt ──► gemini.py ──► cards.generated.json ──► (you review) ──► main.py --file

```

## 💶 Requirements, costs and privacy

- Python 3
- [Anki Desktop](https://apps.ankiweb.net/) with the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on
- A Google Gemini API key and an ElevenLabs API key

Both services have their own pricing and limits. Check them before generating many cards.

**Privacy:** the English sentences (and any text you pass to `--generate`) are sent to Google (Gemini) and ElevenLabs. Your cards and audio stay in Anki (and in AnkiWeb if you sync).

## 🔌 Installing AnkiConnect

1. Open Anki Desktop and go to **Tools → Add-ons → Get Add-ons...**
2. Enter the code `2055492159` and restart Anki.
3. Keep Anki open while the script runs. AnkiConnect listens on `http://127.0.0.1:8765`.

**Security note:** keep AnkiConnect restricted to local applications. Do not expose it to the internet.

## 🚀 Getting Started

### 1. Clone and install

```bash
git clone https://github.com/djara-it/anki-english-workflow.git
cd anki-english-workflow
python -m venv .venv

```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

```

Install the dependencies:

```bash
pip install -r requirements.txt

```

### 2. Add your API keys

```bash
# Windows: copy .env.example .env
cp .env.example .env

```

Open `.env` and fill in your keys:

```text
GEMINI_API_KEY="your_gemini_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_key_here"

```

Never commit `.env`. It is already listed in `.gitignore`.

### 3. Configure Anki

The script expects a note type with the fields `Anverso` (front) and `Reverso` (back). The default Spanish "Básico" note type has them. Set your deck and note type in `config.json`:

```json
{
  "deck": "Inglés práctico",
  "model": "Básico"
}

```

### 4. Prepare your flashcards

Add your cards to `cards.json`:

```json
[
  {
    "front": "I'm gonna wait in the lobby.",
    "back": "Voy a esperar en el vestíbulo.",
    "pronunciation": "Aim gona ueit in dha labi",
    "tags": ["english", "daily"]
  }
]

```

All four fields are required. Cards with missing or invalid fields are skipped with a warning. The pronunciation field is an AI-generated approximation, not IPA. Rely on the audio.

### 5. Run it

With Anki open:

```bash
python main.py

```

Example output:

```text
Resumen:
Creadas: 1
Ya existentes: 3
Audios añadidos: 0
Errores: 0

```

## 🤖 Generate cards with Gemini (optional)

Put some English text in a file and let Gemini turn it into cards. This does not touch Anki:

```bash
python main.py --generate texto.txt

```

Review `cards.generated.json`, then import it:

```bash
python main.py --file cards.generated.json

```

## 📁 Project Structure

```text
anki-english-workflow/
├── main.py            # workflow: Anki lookup, audio generation, card creation
├── gemini.py          # raw text -> card JSON with Gemini
├── cards.json         # your cards
├── config.json        # deck and note type
├── requirements.txt
├── .env.example
├── LICENSE
└── tests/             # manual scripts (see below)

```

## 🧪 Testing

The scripts in `tests/` are **manual checks** that can call the real Anki, ElevenLabs and Gemini services, and one of them uses a hard-coded note ID. **Do not run** `pytest` **on this folder.** Run a single script by hand if you need it:

```bash
python tests/test_elevenlabs.py

```

Planned: automated tests with mocked AnkiConnect and TTS responses, so they run without keys or Anki.

## ⚠️ Known limitations

- The duplicate check searches the `Anverso` field, even if you change the field names in `config.json`.
- Only one deck and one note type are supported through `config.json`.

## 🗺️ Roadmap

- Automated tests with mocks and a CI workflow.
- Pin dependency versions.
- Configurable voice and model names.

## 👨‍💻 About the Developer

I'm a self-taught developer building practical projects to improve my skills in Python, automation and software development. I learn by building, testing and improving each project step by step. Anki English Workflow is part of that journey.

## 🔗 Resources

- [Anki](https://apps.ankiweb.net/)
- [AnkiConnect on AnkiWeb](https://ankiweb.net/shared/info/2055492159)
- [Google AI Studio](https://aistudio.google.com/)
- [ElevenLabs](https://elevenlabs.io/)

## 📄 License

MIT. See [LICENSE](https://claude.ai/chat/LICENSE).