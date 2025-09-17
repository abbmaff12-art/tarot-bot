class SpiritMessageEngine:
    def __init__(self):
        pass

    def channel(self, cards):
        # Simple poetic synthesis from spiritual lessons
        lines = [card.data.get("spiritual_lesson", "[no lesson]") for card in cards]
        return "“" + " ".join(lines) + "”"