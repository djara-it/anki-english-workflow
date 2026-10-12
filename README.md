<h1 align="center">Anki English Workflow</h1>

<div align="center">

  <a href="[https://www.python.org"><img](https://www.python.org"><img) src="[https://img.shields.io/badge/Python-3.10%2B-blue.svg](https://img.shields.io/badge/Python-3.10%2B-blue.svg)" alt="Python"></a>

  <a href="[https://ai.google.dev/"><img](https://ai.google.dev/"><img) src="[https://img.shields.io/badge/Google-Gemini-orange.svg](https://img.shields.io/badge/Google-Gemini-orange.svg)" alt="Google Gemini"></a>

  <a href="[https://elevenlabs.io/"><img](https://elevenlabs.io/"><img) src="[https://img.shields.io/badge/ElevenLabs-TTS-purple.svg](https://img.shields.io/badge/ElevenLabs-TTS-purple.svg)" alt="ElevenLabs"></a>

  <a href="[https://foosoft.net/projects/anki-connect/"><img](https://foosoft.net/projects/anki-connect/"><img) src="[https://img.shields.io/badge/AnkiConnect-API-green.svg](https://img.shields.io/badge/AnkiConnect-API-green.svg)" alt="AnkiConnect"></a>

  <a href="LICENSE"><img src="[https://img.shields.io/badge/License-MIT-yellow.svg](https://img.shields.io/badge/License-MIT-yellow.svg)" alt="License"></a>

  <p><em>AI-powered English learning automation designed to eliminate repetitive friction in spaced repetition.</em></p>

</div>

<hr>

<h2>The Problem & The Goal</h2>

<blockquote>

  <p><em>"Learning English should take time. Managing flashcards shouldn't."</em></p>

</blockquote>

<p>Creating useful Anki cards manually is a repetitive burden: selecting expressions, writing translations, mapping pronunciation tags, searching for audio clips, and verifying duplicates.</p>

<p><strong>Anki English Workflow</strong> acts as an intelligent automation layer. Python orchestrates the pipeline, generative AI handles language understanding, and Anki remains the core spaced-repetition learning environment.</p>

<hr>

<h2>Core Features</h2>

<ul>

  <li><strong>Intelligent Card Generation:</strong> Transforms raw text into structured JSON data using <strong>Google Gemini</strong>.</li>

  <li><strong>Dual TTS with Fallback:</strong> Native, high-quality speech generation via <strong>ElevenLabs</strong>, featuring automatic failover to <strong>Gemini TTS</strong> if quotas or connection limits are reached.</li>

  <li><code>Smart Duplicate Protection:</code> Automatically queries Anki via <strong>AnkiConnect</strong> to skip pre-existing entries and missing-audio updates safely.</li>

  <li><strong>Dynamic Configuration:</strong> Fully decoupled via <code>config.json</code> to handle custom decks, models, and customizable flashcard fields.</li>

  <li><strong>In-Memory Audio Pipeline:</strong> Generates and transfers media bytes directly into Anki via deterministic <code>SHA-256</code> hashing without workspace clutter.</li>

</ul>

<hr>

<h2>Architecture & Data Flow</h2>

<pre><code>English Input ──► Gemini AI ──► cards.json ──► Python Orchestrator

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

             Anki Deck ("Inglés práctico")</code></pre>

<hr>

<h2>Project Structure</h2>

<pre><code>anki-english-workflow/

├── [main.py](http://main.py)             # Core automation and orchestration engine

├── [gemini.py](http://gemini.py)           # Google Gemini AI card generator integration

├── cards.json          # Intermediate structured card storage

├── config.json         # Flexible local preferences and field mappings

├── requirements.txt    # Pinned stable Python dependencies

├── .env.example        # Template for environment variables

└── tests/              # Automated unit tests and mock integrations</code></pre>

<hr>

<h2>Setup & Installation</h2>

<h3>1. Clone the repository</h3>

<pre><code>git clone [https://github.com/djara-it/anki-english-workflow.git](https://github.com/djara-it/anki-english-workflow.git)

cd anki-english-workflow</code></pre>

<h3>2. Set up the Python Environment</h3>

<pre><code>python -m venv .venv

source .venv/Scripts/activate  # En Git Bash (Windows)</code></pre>

<h3>3. Install Dependencies</h3>

<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Configure AnkiConnect</h3>

<ol>

  <li>Open <strong>Anki Desktop</strong>.</li>

  <li>Go to <strong>Tools → Add-ons → Get Add-ons</strong>.</li>

  <li>Paste code: <code>2055492159</code> (AnkiConnect) and restart Anki.</li>

</ol>

<h3>5. Environment Variables (.env)</h3>

<pre><code>copy .env.example .env  # Windows</code></pre>

<p>Open <code>.env</code> and add your secure API keys:</p>

<pre><code>GEMINI_API_KEY="your_gemini_api_key_here"

ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"</code></pre>

<h3>6. Adjust config.json</h3>

<pre><code>{

    "deck": "Inglés práctico",

    "model": "Básico",

    "field_front": "Anverso",

    "field_back": "Reverso"

}</code></pre>

<hr>

<h2>Usage & Testing</h2>

<ul>

  <li><strong>Run the main workflow:</strong> <code>python [main.py](http://main.py)</code></li>

  <li><strong>Run automated test suites:</strong> <code>pytest</code></li>

</ul>

<hr>

<h2>Security & Privacy</h2>

<ul>

  <li><strong>Local Secrets:</strong> API keys are strictly restricted to your local <code>.env</code> file and ignored by Git.</li>

  <li><strong>No External DB:</strong> Keeps complete privacy using exclusively Anki's local database.</li>

</ul>

<hr>

<h2>License</h2>

<p>Distributed under the <strong>MIT License</strong>. See <a href="LICENSE">LICENSE</a> for more details.</p>

