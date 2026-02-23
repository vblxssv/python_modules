import random
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        if total == 0:
            return {'total_cards': 0, 'creatures': 0, 'spells': 0,
                    'artifacts': 0, 'avg_cost': 0.0}

        creatures = sum(1 for c in self.cards if isinstance(c, CreatureCard))
        spells = sum(1 for c in self.cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.cards if isinstance(c, ArtifactCard))
        avg_cost = sum(c.cost for c in self.cards) / total

        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(float(avg_cost), 1)
        }
