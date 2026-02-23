from ex0.Card import Card
from enum import Enum


class Effect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """Concrete implementation of a spell card"""
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """
        Execute the spell using available mana.
        Returns a dictionary describing the effect.
        """
        if not self.is_playable(game_state.get("mana", 0)):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        game_state["mana"] -= self.cost

        effect_result = self.resolve_effect(game_state.get("targets", []))
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_result["effect"]
        }

    def resolve_effect(self, targets: list) -> dict:
        """
        Returns the spell effect.
        For demonstration, we assume damage = cost.
        """
        target_name = targets[0] if targets else "target"
        if self.effect_type == Effect.DAMAGE:
            return {"effect": f"Deal {self.cost} damage to {target_name}"}
        elif self.effect_type == Effect.HEAL:
            return {"effect": f"Heal {self.cost} health to {target_name}"}
        elif self.effect_type == Effect.BUFF:
            return {"effect": f"Buff {target_name} by {self.cost}"}
        elif self.effect_type == Effect.DEBUFF:
            return {"effect": f"Debuff {target_name} by {self.cost}"}
        else:
            return {"effect": "Unknown effect"}
