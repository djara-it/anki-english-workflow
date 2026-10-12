# Anki English Workflow

  **Automate your English-learning workflow with Python, AI, and Anki.**

  A personal project that combines programming and language learning

  to simplify flashcard creation and improve the daily English-learning experience. 

```
<img src="[https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)" alt="Python">
```

```
<img src="[https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)" alt="Google Gemini">
```

```
<img src="[https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logo=elevenlabs&logoColor=white](https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logo=elevenlabs&logoColor=white)" alt="ElevenLabs">
```

```
<img src="[https://img.shields.io/badge/AnkiConnect-2D8CFF?style=for-the-badge&logo=anki&logoColor=white](https://img.shields.io/badge/AnkiConnect-2D8CFF?style=for-the-badge&logo=anki&logoColor=white)" alt="AnkiConnect">
```

![License]([https://img.shields.io/badge/License-See%20LICENSE%20file-lightgrey?style=for-the-badge](https://img.shields.io/badge/License-See%20LICENSE%20file-lightgrey?style=for-the-badge))

---



## 🎬 Project Demo

**See the workflow in action.**

[https://github.com/user-attachments/assets/10d77069-8d28-48fe-9d52-d90dcf9a6bb9](https://github.com/user-attachments/assets/10d77069-8d28-48fe-9d52-d90dcf9a6bb9)

## 📌 About the Project

**Anki English Workflow** is a Python project designed to reduce the manual work involved in creating and managing English-learning flashcards in Anki.

The project uses structured JSON data and AnkiConnect to communicate with a local Anki installation. It is also an opportunity to apply practical software development concepts, including automation, configuration management, duplicate detection, and error handling.

The long-term goal is to create a more efficient workflow for turning useful English expressions into organized, ready-to-study flashcards.

## ✨ Features

- 🤖 **AI-assisted content creation:** Prepare structured English-learning content with AI tools.
- ⚡ **Flashcard automation:** Process flashcard data and send notes to Anki through AnkiConnect.
- 🔄 **Duplicate prevention:** Check for existing notes to avoid unnecessary duplicates.
- 🗂️ **JSON-based data management:** Keep flashcards and application settings in separate files.
- ⚙️ **Configurable workflow:** Manage project settings without mixing them with the main application logic.
- 📊 **Processing feedback:** Track created notes, existing notes, and errors.
- 📚 **Practical English learning:** Organize useful expressions, translations, and pronunciation guides for everyday situations.



## 🛠️ Tech Stack


| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Application logic and automation    |
| Google Gemini | AI-assisted content generation      |
| ElevenLabs    | Voice and pronunciation workflows   |
| Anki          | Spaced-repetition flashcards        |
| AnkiConnect   | Communication with Anki Desktop     |
| JSON          | Flashcard data and configuration    |
| Git & GitHub  | Version control and project hosting |


*The role of each integration depends on the components enabled in the current implementation.*

## 🔄 How It Works

The workflow is designed to connect English-learning content with your Anki collection.

1. **Generate content:** Prepare useful English phrases, translations, and pronunciation guides.
2. **Structure the data:** Organize the flashcards in `cards.json`.
3. **Load configuration:** Read the settings from `config.json`.
4. **Connect to Anki:** Use AnkiConnect to communicate with the local Anki application.
5. **Check for duplicates:** Identify notes that already exist before creating new ones.
6. **Process the cards:** Create eligible notes and report the results.
7. **Study and review:** Use Anki's spaced-repetition system to practice consistently.



## 🔌 Installing AnkiConnect

AnkiConnect allows Python applications to communicate with Anki Desktop through a local API.

### 1. Install AnkiConnect

1. Open Anki Desktop.
2. Navigate to **Tools → Add-ons**.
3. Select **Get Add-ons...**
4. Enter the official AnkiConnect add-on code:
  `2055492159`
5. Confirm the installation and restart Anki.

You can also visit the official add-on page:

**[Download AnkiConnect from AnkiWeb](https://ankiweb.net/shared/info/2055492159)**

### 2. Verify the connection

Make sure Anki Desktop is running. AnkiConnect normally listens on:

`http://127.0.0.1:8765`

Your Python application can use this local endpoint to communicate with Anki.

**Security note:** Keep AnkiConnect's access restricted to trusted local applications. Do not expose its API directly to the public internet.

## 🚀 Getting Started



### Prerequisites

Before running the project, make sure you have:

- Python installed.
- [Anki Desktop](https://apps.ankiweb.net/) installed.
- [AnkiConnect](https://ankiweb.net/shared/info/2055492159) installed and configured.
- Git installed if you want to clone the repository.



### 1. Clone the repository

```
git clone https://github.com/djara-it/anki-english-workflow.git
cd anki-english-workflow
```



### 2. Configure AnkiConnect

Open Anki Desktop and verify that AnkiConnect is installed and responding.

The default local API address is:

```
http://127.0.0.1:8765
```

Make sure the connection settings in `config.json` match the application's expected configuration.

### 3. Prepare your flashcards

Add your flashcards to `cards.json` using the expected data structure.

Example:

```
[
  {
    "front": "I'm gonna wait in the lobby.",
    "back": "Voy a esperar en el vestíbulo.",
    "pronunciation": "Aim gona ueit in dha labi",
    "tags": ["english", "daily"]
  }
]
```

This example illustrates the learning-content format. The fields actually processed by the application depend on its implementation and configuration.

### 4. Run the application

From the project directory, run:

```
python main.py
```

Ensure Anki Desktop is running and your configuration is correct before processing your cards.

> If the project requires additional dependencies, install them according to the dependency instructions included in the repository.



## 📁 Project Structure

```
anki-english-workflow/
├── main.py
├── cards.json
├── config.json
├── README.md
└── .gitignore
```

- `main.py` — Main application and processing workflow.
- `cards.json` — Structured flashcard data.
- `config.json` — Application configuration.
- `.gitignore` — Files and directories excluded from Git.
- `README.md` — Project documentation.



## 🧪 Reliability and Testing

Reliability is an important part of the project.

The development focus includes:

- Preventing duplicate note creation.
- Handling invalid data and API errors.
- Keeping application settings separate from processing logic.
- Verifying that the workflow behaves as expected.
- Improving maintainability through automated tests and incremental changes.



## 🗺️ Roadmap

Potential areas for future development include:

- Improve onboarding and installation documentation.
- Expand automated test coverage.
- Improve error reporting and recovery.
- Streamline the workflow from AI-generated content to Anki.
- Improve support for pronunciation and audio learning.
- Make the project easier to configure and use on a fresh installation.



## 🎯 Why This Project?

Learning to program is more effective when theory is applied to practical problems.

This project combines a real personal need — making English practice easier — with hands-on development in Python, API integration, structured data, testing, and automation.

The objective is not simply to make a script work, but to build a tool that becomes more reliable, maintainable, and useful over time.

## 👨‍💻 About the Developer

I'm a self-taught developer building practical projects to improve my skills in Python, automation, and software development.

I focus on learning by building, testing, understanding the underlying code, and improving each project incrementally.

Anki English Workflow is part of that journey.

## 🔗 Resources

- [GitHub Repository](https://github.com/djara-it/anki-english-workflow)
- [Anki Official Website](https://apps.ankiweb.net/)
- [AnkiConnect on AnkiWeb](https://ankiweb.net/shared/info/2055492159)
- [Google AI Studio](https://aistudio.google.com/)
- [ElevenLabs](https://elevenlabs.io/)

---

**Built with Python, curiosity, and a commitment to continuous learning.**