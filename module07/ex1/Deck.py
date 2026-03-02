import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Class to manage a collection of various card types."""

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by its name. Returns True if successful."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomize the order of cards in the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Remove and return the top card from the deck."""
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Calculate and return statistics about the deck's composition."""
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
