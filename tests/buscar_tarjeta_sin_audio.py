import main


def buscar_tarjeta_sin_audio():
    data = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": 'deck:"Inglés práctico"'
        }
    }

    result = main.anki_request(data)

    if result["error"] is not None:
        print("ERROR:", result["error"])
        return

    note_ids = result["result"]

    print("Tarjetas encontradas:", len(note_ids))
    print()

    encontradas = 0

    for note_id in note_ids:
        note = main.get_note(note_id)

        if note is None:
            continue

        front = note["fields"]["Anverso"]["value"]
        reverso = note["fields"]["Reverso"]["value"]

        if "[sound:" not in reverso:
            print("TARJETA SIN AUDIO:")
            print("ID:", note_id)
            print("Anverso:", front)
            print()
            encontradas += 1

            if encontradas >= 5:
                break

    if encontradas == 0:
        print("Todas las tarjetas encontradas ya tienen audio.")


if __name__ == "__main__":
    buscar_tarjeta_sin_audio()