from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract Base Class defining the universal blueprint for all cards."""

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Execute card effect and return updated game state."""
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary containing basic card information."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with the current mana."""
        return self.cost <= available_mana
