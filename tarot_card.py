class TarotCard:
    def __init__(self, name, orientation, data):
        self.name = name
        self.orientation = orientation  # 'upright' or 'reversed'
        self.data = data

    @classmethod
    def from_db(cls, name, orientation, kb):
        card_data = kb.get(name, {})
        orientation_data = card_data.get(orientation, {})
        return cls(name, orientation, orientation_data)
