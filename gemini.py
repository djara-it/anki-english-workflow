import os
import json
from google import genai


def generate_cards(text):
    api_key = os.environ.get("GEMINI_API_KEY")

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

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return json.loads(interaction.output_text)