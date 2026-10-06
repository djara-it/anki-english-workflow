from gemini import generate_cards


text = """
I'm just looking around.
Could I pick it up in 20 minutes?
There's a scratch on the car.
"""

result = generate_cards(text)

print(result)