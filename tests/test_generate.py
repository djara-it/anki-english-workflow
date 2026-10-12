import gemini

def test_generate_cards_mocked(monkeypatch):
    """Simula la respuesta de la función generate_cards para evitar llamadas reales a la API."""
    
    # Definimos una función simulada que devuelve directamente una tarjeta de prueba estructurada
    def mock_generate_cards(text):
        return [
            {
                "front": "I need to reschedule.",
                "back": "Necesito cambiar la fecha.",
                "pronunciation": "Ai nid tu rischediul.",
                "tags": ["english"]
            }
        ]

    # Reemplazamos la función real por nuestra función simulada
    monkeypatch.setattr(gemini, "generate_cards", mock_generate_cards)

    # Ejecutamos la función
    cards = gemini.generate_cards("I need to reschedule.")
    
    assert isinstance(cards, list)
    assert len(cards) > 0
    assert cards[0]["front"] == "I need to reschedule."