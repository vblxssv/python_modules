import random
from typing import Dict, List, Union, Optional
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory

class FantasyCardFactory(CardFactory):
    """
    Concrete factory for Fantasy-themed cards.
    Implements extensible registration for creatures, spells, and artifacts.
    """

    def __init__(self):
        self._registry = {
            "creatures": ["Dragon", "Goblin", "Orc", "Troll"],
            "spells": ["Fireball", "Ice Nova", "Lightning Bolt"],
            "artifacts": ["Mana Ring", "Staff of Power", "Crystal Ball"]
        }

    def _get_random_rarity(self) -> str:
        return random.choice(list(Rarity)).value

    def create_creature(self, name_or_power: Optional[Union[str, int]] = None) -> Card:
        """Creates a fantasy creature (Dragon, Goblin, etc.)"""
        # Logic for extensible naming
        if isinstance(name_or_power, str):
            name = name_or_power
        else:
            name = random.choice(self._registry["creatures"])
            
        # If power (int) is provided, use it for attack/health, otherwise random
        power = name_or_power if isinstance(name_or_power, int) else random.randint(1, 10)
        cost = max(1, power // 2 + random.randint(0, 2))
        
        return CreatureCard(
            name=name,
            cost=cost,
            rarity=self._get_random_rarity(),
            attack=power,
            health=max(1, power + random.randint(-1, 2))
        )

    def create_spell(self, name_or_power: Optional[Union[str, int]] = None) -> Card:
        """Creates elemental spells (Fire, Ice, Lightning)"""
        name = name_or_power if isinstance(name_or_power, str) else random.choice(self._registry["spells"])
        cost = name_or_power if isinstance(name_or_power, int) else random.randint(1, 5)
        
        # Using a generic Card implementation for Spell
        return type("SpellCard", (Card,), {"play": lambda s, gs: {"played": s.name}})(
            name, cost, self._get_random_rarity()
        )

    def create_artifact(self, name_or_power: Optional[Union[str, int]] = None) -> Card:
        """Creates magical artifacts (Rings, Staffs, Crystals)"""
        name = name_or_power if isinstance(name_or_power, str) else random.choice(self._registry["artifacts"])
        cost = name_or_power if isinstance(name_or_power, int) else random.randint(1, 4)
        
        return type("ArtifactCard", (Card,), {"play": lambda s, gs: {"played": s.name}})(
            name, cost, self._get_random_rarity()
        )

    def create_themed_deck(self, size: int) -> dict:
        """Generates a balanced fantasy deck."""
        deck = []
        for _ in range(size):
            # Mix creatures, spells, and artifacts
            choice = random.random()
            if choice < 0.6:
                deck.append(self.create_creature())
            elif choice < 0.8:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        
        return {
            "deck": deck,
            "count": len(deck),
            "theme": "Fantasy"
        }

    def get_supported_types(self) -> dict:
        """Supports extensible card type registration check."""
        return self._registry

    def register_new_type(self, category: str, name: str):
        """Method to support extensibility: add new names to categories."""
        if category in self._registry:
            if name not in self._registry[category]:
                self._registry[category].append(name)