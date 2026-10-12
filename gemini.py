import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).resolve().parent / ".env")


def generate_cards(text):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("ERROR: No se encontró la variable de entorno GEMINI_API_KEY en el archivo .env")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Create English Anki cards from the following text:

{text}

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations.

Return a JSON object with this exact structure:

{{
  "cards": [
    {{
      "front": "English sentence",
      "back": "Spanish translation",
      "pronunciation": "Natural pronunciation approximation",
      "tags": ["tag1"]
    }}
  ]
}}

Only include useful English expressions or sentences.
"""

    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )
        response_text = interaction.output_text
    except Exception as e:
        print(f"ERROR al conectar con la API de Gemini: {e}")
        return {"cards": []}

    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: La respuesta de Gemini no tiene un formato JSON válido: {e}")
        print(f"Respuesta recibida: {response_text}")
        return {"cards": []}