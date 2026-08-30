\# Anki English Workflow



A Python tool that automates the creation of English learning cards in Anki through AnkiConnect.



\## What it does



The program:



\- Reads English cards from a JSON file.

\- Reads the Anki deck and note type from a configuration file.

\- Checks whether each card already exists.

\- Creates only new cards.

\- Reports created cards, existing cards, and errors.



\## How it works



```text

cards.json

&#x20;   ↓

Python

&#x20;   ↓

Check existing notes

&#x20;   ↓

Create only new notes

&#x20;   ↓

AnkiConnect

&#x20;   ↓

Anki

```



\## Project structure



```text

anki-english-workflow/

│

├── main.py          # Main program

├── cards.json       # English cards

├── config.json      # Anki configuration

├── README.md        # Project documentation

├── .gitignore       # Files ignored by Git

└── .venv/           # Python virtual environment

```



\## Requirements



\- Python

\- Anki

\- AnkiConnect



\## Current status



Version 1 — Functional



The current version can read cards from JSON, detect existing cards, create new cards in Anki, and report errors.



\## Future goal



The long-term goal is to integrate the workflow with an external interface so that English learning cards can be sent to Anki automatically without manually editing `cards.json`.



\## Disclaimer



This project is a personal learning project focused on Python, APIs, automation, and Anki integration.

