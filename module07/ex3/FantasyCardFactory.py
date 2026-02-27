import random
from typing import Union, Optional
from ex0.main import Rarity
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory for Fantasy-themed cards."""

    def __init__(self):
        self._registry = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }

    def _get_random_rarity(self) -> str:
        return random.choice(list(Rarity)).value

    def create_creature(self, name_or_power:
                        Optional[Union[str, int]] = None) -> Card:
        """Create a fantasy creature."""
        name = (name_or_power if isinstance(name_or_power, str)
                else random.choice(self._registry["creatures"]))
        power = (name_or_power if isinstance(name_or_power, int)
                 else random.randint(3, 8))
        return CreatureCard(name.title(), power, self._get_random_rarity(),
                            power, max(1, power - 1))

    def create_spell(self, name_or_power:
                     Optional[Union[str, int]] = None) -> Card:
        """Create an elemental spell."""
        name = "fireball"
        cost = (name_or_power if isinstance(name_or_power, int)
                else random.randint(1, 5))
        return type("Spell", (Card,), {"play": lambda s, g: None})(
            name.title(), cost, self._get_random_rarity())

    def create_artifact(self, name_or_power:
                        Optional[Union[str, int]] = None) -> Card:
        """Create a magical artifact."""
        name = "mana_ring"
        cost = 2
        return type("Artifact", (Card,), {"play": lambda s, g: None})(
            name.title(), cost, self._get_random_rarity())

    def create_themed_deck(self, size: int) -> dict:
        """Generate fantasy hand/deck."""
        deck = [self.create_creature() for _ in range(size - 1)]
        deck.append(self.create_spell())
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        """Return registry."""
        return self._registry
