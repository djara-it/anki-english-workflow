import os
from elevenlabs.client import ElevenLabs

api_key = os.environ.get("ELEVENLABS_API_KEY")

if not api_key:
    print("ERROR: No se encontró ELEVENLABS_API_KEY.")
    exit()

client = ElevenLabs(api_key=api_key)

audio = client.text_to_speech.convert(
    text="Would you like to try it on?",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_v4",
    output_format="mp3_44100_128",
)

with open("test_elevenlabs.mp3", "wb") as file:
    for chunk in audio:
        file.write(chunk)

print("Audio creado correctamente: test_elevenlabs.mp3")