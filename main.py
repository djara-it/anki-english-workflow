import urllib.request
import json


def load_cards():
    with open("cards.json", "r", encoding="utf-8") as file:
        cards = json.load(file)

    return cards

def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    return cards


def anki_request(data):
    json_data = json.dumps(data).encode("utf-8")

    url = "http://127.0.0.1:8765"

    request = urllib.request.Request(
        url,
        data=json_data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request) as response:
        result = response.read()

    result = result.decode("utf-8")
    result = json.loads(result)

    return result


def find_note(front):
    data = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": f'"{front}"'
        }
    }

    result = anki_request(data)

    

    if result["error"] is not None:
        print("Error al buscar:", result["error"])
        return None

    return result["result"]

def create_note(card, config):
    data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": config["deck"],
                "modelName": config["model"],
                "fields": {
                    "Anverso": card["front"],
                    "Reverso": card["back"]
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
    errors = 0
    for card in cards:
        front = card["front"]
   

        notes = find_note(front)


        if notes:
            print("YA EXISTE:", front)
            existing += 1
        else:
            print("NO EXISTE:", front)

            result = create_note(card,config)

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
    print("Errores:", errors)      

cards = load_cards()
config = load_config()

process_cards(cards, config)