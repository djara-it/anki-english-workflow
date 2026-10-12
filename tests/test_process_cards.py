
import main


CARD = {
    "front": "I'm gonna wait in the lobby.",
    "back": "Voy a esperar en el vestíbulo.",
    "pronunciation": "Aim gona ueit in da lóbi",
    "tags": ["english", "daily"],
}

CONFIG = {
    "deck": "Test Deck",
    "model": "Básico",
}


def test_existing_card_is_not_created(monkeypatch):
    """Una tarjeta existente no debe volver a crearse."""

    monkeypatch.setattr(main, "find_note", lambda front: [123])

    monkeypatch.setattr(
        main,
        "get_note",
        lambda note_id: {
            "fields": {
                "Reverso": {
                    "value": "Traducción [sound:existing.mp3]"
                }
            }
        },
    )

    def unexpected_call(*args, **kwargs):
        raise AssertionError("No debería generar audio ni crear tarjetas.")

    monkeypatch.setattr(main, "generate_audio", unexpected_call)
    monkeypatch.setattr(main, "create_note", unexpected_call)

    main.process_cards([CARD], CONFIG)


def test_missing_card_can_be_created(monkeypatch):
    """Una búsqueda correcta sin resultados permite crear la tarjeta."""

    monkeypatch.setattr(main, "find_note", lambda front: [])

    monkeypatch.setattr(
        main,
        "generate_audio",
        lambda front: {"data": b"fake-audio", "extension": "mp3"},
    )

    monkeypatch.setattr(main, "store_audio", lambda *args: True)

    monkeypatch.setattr(
        main,
        "create_note",
        lambda *args: {"result": 456, "error": None},
    )

    main.process_cards([CARD], CONFIG)


def test_failed_search_does_not_create_card(monkeypatch):
    """Si falla la búsqueda, no se debe crear una tarjeta."""

    monkeypatch.setattr(main, "find_note", lambda front: None)

    def unexpected_call(*args, **kwargs):
        raise AssertionError(
            "No debería generar audio ni crear tarjetas si falla la búsqueda."
        )

    monkeypatch.setattr(main, "generate_audio", unexpected_call)
    monkeypatch.setattr(main, "create_note", unexpected_call)

    main.process_cards([CARD], CONFIG)
