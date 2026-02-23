from ex0.Card import Card
from enum import Enum


class Effect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class ArtifactCard(Card):
    """Concrete implementation of an artifact card (permanent modifier)"""
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """
        Plays the artifact: deducts mana and activates permanent effect.
        """
        if not self.is_playable(game_state.get("mana", 0)):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play artifact"
            }
        game_state["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        """
        Activates the ongoing ability of the artifact.
        """
        if self.durability <= 0:
            return {"effect": (f"{self.name} is destroyed, "
                               f"cannot activate ability")}
        return {"effect": f"{self.name} ability activated: {self.effect}"}
