class TarotInterpreter:
    def __init__(self, kb):
        self.kb = kb

    def interpret(self, cards):
        messages = []
        for card in cards:
            meaning = card.data.get("interpretations", ["[No meaning found]"])[0]
            messages.append(f"{card.name} ({card.orientation}): {meaning}")
        return messages
