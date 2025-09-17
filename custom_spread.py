import re
from tarot_card import TarotCard

class CustomSpreadInterpreter:
    def __init__(self, kb):
        self.kb = kb

    def parse_input(self, user_input):
        pattern = r'([A-Za-z0-9 ]+)\s*\((upright|reversed)\)'
        found = re.findall(pattern, user_input, re.IGNORECASE)
        return [
            TarotCard(name.strip(), orientation.lower(), self.kb.get(name.strip(), {}).get(orientation.lower(), {}))
            for name, orientation in found
        ]
