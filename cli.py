import json
from custom_spread import CustomSpreadInterpreter
from interpreter import TarotInterpreter
from spirit_message import SpiritMessageEngine

def main():
    with open("knowledge_base.json") as f:
        kb = json.load(f)

    print("Welcome to TarotBot! Type your card draw in this format:")
    print("Example: The Tower (reversed), Ace of Cups (upright), 7 of Pentacles (upright)")
    user = input("Your draw: ")

    spread = CustomSpreadInterpreter(kb)
    cards = spread.parse_input(user)
    interp = TarotInterpreter(kb)
    spirit = SpiritMessageEngine()

    print("\nReading:")
    for idx, card in enumerate(cards, 1):
        print(f"> Card {idx}: {card.name} ({card.orientation}) – {card.data.get('interpretations', ['[No meaning]'])[0]}")
    print("\n> Spirit Message:")
    print(spirit.channel(cards))

if __name__ == "__main__":
    main()