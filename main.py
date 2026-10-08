import urllib.error
import urllib.request
import json
import os
import base64
import hashlib
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from elevenlabs.client import ElevenLabs

load_dotenv(Path(__file__).resolve().parent / ".env")

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
ANKI_REQUEST_TIMEOUT = 15

def load_cards():
    with open("cards.json", "r", encoding="utf-8") as file:
        cards = json.load(file)

    return cards


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    return config


def anki_request(data):
    json_data = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        ANKI_CONNECT_URL,
        data=json_data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=ANKI_REQUEST_TIMEOUT
        ) as response:
            status = response.status
            raw_response = response.read()
    except TimeoutError:
        print("Timeout al conectar con AnkiConnect.")
        return {
            "result": None,
            "error": "Timeout al conectar con AnkiConnect."
        }
    except urllib.error.URLError as error:
        print("Error al conectar con AnkiConnect:", error.reason)
        return {
            "result": None,
            "error": "No se pudo conectar con AnkiConnect."
        }

    if status != 200:
        print("Respuesta HTTP inválida de AnkiConnect:", status)
        return {
            "result": None,
            "error": f"HTTP {status}"
        }

    try:
        result = json.loads(raw_response.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        print("AnkiConnect no devolvió JSON válido.")
        return {
            "result": None,
            "error": "Respuesta de AnkiConnect no es JSON válido."
        }

    if not isinstance(result, dict):
        print("Respuesta de AnkiConnect con formato incorrecto.")
        return {
            "result": None,
            "error": "Respuesta de AnkiConnect con formato incorrecto."
        }

    if "result" not in result or "error" not in result:
        print("Respuesta de AnkiConnect incompleta.")
        return {
            "result": None,
            "error": "Respuesta de AnkiConnect incompleta."
        }

    return result


def escape_anki_query_value(value):
    escaped = (
        value
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("*", "\\*")
        .replace("_", "\\_")
    )

    return escaped


def find_note(front):
    safe_front = escape_anki_query_value(front)

    data = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f'Anverso:"{safe_front}"'
        }
    }

    result = anki_request(data)

    if result["error"] is not None:
        print("Error al buscar:", result["error"])
        return None

    return result["result"]


def get_note(note_id):
    data = {
        "action": "notesInfo",
        "version": 6,
        "params": {
            "notes": [note_id]
        }
    }

    result = anki_request(data)

    if result["error"] is not None:
        print("Error al obtener tarjeta:", result["error"])
        return None

    if not result["result"]:
        return None

    return result["result"][0]

def generate_audio(front):
    print("Generando audio con ElevenLabs...")

    # ==========================================
    # 1. INTENTAR ELEVENLABS
    # ==========================================

    elevenlabs_key = os.environ.get("ELEVENLABS_API_KEY")

    if elevenlabs_key:
        try:
            client = ElevenLabs(api_key=elevenlabs_key)

            audio = client.text_to_speech.convert(
                text=front,
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                model_id="eleven_v4",
                output_format="mp3_44100_128",
            )

            audio_data = b"".join(audio)

            print("Audio generado con ElevenLabs en memoria.")

            return {
                "data": audio_data,
                "extension": "mp3"
            }

        except Exception as error:
            print("ElevenLabs no disponible.")
            print("Motivo:", error)
            print("Intentando Gemini...")

    else:
        print("No se encontró ELEVENLABS_API_KEY.")
        print("Intentando Gemini...")

    # ==========================================
    # 2. INTENTAR GEMINI COMO FALLBACK
    # ==========================================

    gemini_key = os.environ.get("GEMINI_API_KEY")

    if not gemini_key:
        print("ERROR: No se encontró GEMINI_API_KEY.")
        return None

    try:
        client = genai.Client(
            api_key=gemini_key,
            http_options={
                "timeout": 10000
            }
        )

        response = client.interactions.create(
            model="gemini-3.8-flash-tts",
            input=[
                {
                    "type": "user_input",
                    "content": [
                        {
                            "type": "text",
                            "text": front,
                            "annotations": [
                                {
                                    "type": "speech_metadata",
                                    "style": "natural, conversational American English",
                                }
                            ],
                        }
                    ],
                }
            ],
            response_format={
                "type": "audio"
            },
            generation_config={
                "speech_config": [
                    {
                        "voice": "Kore"
                    }
                ]
            },
        )

        audio_data = base64.b64decode(response.output_audio.data)

        print("Audio generado con Gemini en memoria.")

        return {
            "data": audio_data,
            "extension": "wav"
        }

    except Exception as error:
        print("Gemini no pudo generar el audio.")
        print("Motivo:", error)
        return None
    
def store_audio(audio_data, filename):
    print("Guardando audio en Anki...")

    audio_base64 = base64.b64encode(audio_data).decode("utf-8")

    data = {
        "action": "storeMediaFile",
        "version": 6,
        "params": {
            "filename": filename,
            "data": audio_base64
        }
    }

    result = anki_request(data)

    if result["error"] is not None:
        print("Error al guardar audio:", result["error"])
        return False

    print("Audio guardado en Anki:", filename)

    return True


def add_audio_to_note(note_id, filename):
    note = get_note(note_id)

    if note is None:
        return False

    reverso_actual = note["fields"]["Reverso"]["value"]

    # No añadir audio si ya existe
    if "[sound:" in reverso_actual:
        print("La tarjeta ya tiene audio.")
        return True

    nuevo_reverso = reverso_actual + f"<br><br>[sound:{filename}]"

    data = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note_id,
                "fields": {
                    "Reverso": nuevo_reverso
                }
            }
        }
    }

    result = anki_request(data)

    if result["error"] is not None:
        print("Error al añadir audio:", result["error"])
        return False

    print("Audio añadido a la tarjeta.")

    return True


def create_note(card, config, audio_filename):
    data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": config["deck"],
                "modelName": config["model"],
                "fields": {
                    "Anverso": card["front"],
                    "Reverso": (
                        f'{card["back"]}'
                        f'<br><br>'
                        f'Pronunciación: {card["pronunciation"]}'
                        f'<br><br>'
                        f'[sound:{audio_filename}]'
                    )
                },
                "tags": card["tags"]
            }
        }
    }

    result = anki_request(data)

    return result


def process_cards(cards, config):
    created = 0
    existing = 0
    audio_added = 0
    errors = 0

    for card in cards:
        front = card["front"]

        print()
        print("Procesando:", front)

        notes = find_note(front)

        if notes:
            print("YA EXISTE:", front)

            existing += 1

            note_id = notes[0]
            note = get_note(note_id)

            if note is None:
                print("ERROR: No se pudo obtener la tarjeta.")
                errors += 1
                continue

            reverso = note["fields"]["Reverso"]["value"]

            if "[sound:" in reverso:
                print("Ya tiene audio. No se modifica.")
                continue

            print("No tiene audio.")

            audio = generate_audio(front)

            if audio is None:
                errors += 1
                continue

            hash_name = hashlib.sha256(front.encode("utf-8")).hexdigest()[:16]
            audio_filename = f"tts_{hash_name}.{audio['extension']}"

            if not store_audio(audio["data"], audio_filename):
                errors += 1
                continue

            if add_audio_to_note(note_id, audio_filename):
                audio_added += 1
            else:
                errors += 1

        else:
            print("NO EXISTE:", front)

            audio = generate_audio(front)

            if audio is None:
                errors += 1
                continue

            hash_name = hashlib.sha256(front.encode("utf-8")).hexdigest()[:16]
            audio_filename = f"tts_{hash_name}.{audio['extension']}"

            if not store_audio(audio["data"], audio_filename):
                errors += 1
                continue

            result = create_note(card, config, audio_filename)

            if result["error"] is None:
                print("CREADA:", front)
                created += 1
            else:
                print("ERROR:", result["error"])
                errors += 1

    print()
    print("Resumen:")
    print("Creadas:", created)
    print("Ya existentes:", existing)
    print("Audios añadidos:", audio_added)
    print("Errores:", errors)


if __name__ == "__main__":
    cards = load_cards()
    config = load_config()

    process_cards(cards, config)