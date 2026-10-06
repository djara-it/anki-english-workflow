import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main

NOTE_ID = 1790958819839


def test():
    print("Buscando tarjeta...")

    note = main.get_note(NOTE_ID)

    if note is None:
        print("ERROR: No se encontró la tarjeta.")
        return

    front = note["fields"]["Anverso"]["value"]
    reverso = note["fields"]["Reverso"]["value"]

    print("Anverso:", front)

    if "[sound:" in reverso:
        print("La tarjeta ya tiene audio. No se hará nada.")
        return

    print("La tarjeta no tiene audio.")
    print()

    audio = main.generate_audio(front)

    if audio is None:
        print("ERROR: No se pudo generar el audio.")
        return

    audio_filename = f"test_memory.{audio['extension']}"

    if not main.store_audio(audio["data"], audio_filename):
        print("ERROR: No se pudo guardar el audio en Anki.")
        return

    if main.add_audio_to_note(NOTE_ID, audio_filename):
        print()
        print("===================================")
        print("PRUEBA COMPLETADA CORRECTAMENTE")
        print("===================================")
        print("Audio:", audio_filename)
    else:
        print("ERROR: No se pudo añadir el audio a la tarjeta.")


if __name__ == "__main__":
    test()