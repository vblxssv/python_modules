from enum import Enum
from ex0.Card import Card


class Effect(Enum):
    """Enumeration of spell effect types."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """Concrete implementation of a spell card for one-time effects."""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Process spell casting logic."""
        current_mana = game_state.get("mana", 0)
        if not self.is_playable(current_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        game_state["mana"] -= self.cost
        targets = game_state.get("targets", [])
        effect_data = self.resolve_effect(targets)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_data["effect"]
        }

    def resolve_effect(self, targets: list) -> dict:
        """Apply the specific spell effect to selected targets."""
        if not targets:
            target_name = "target"
        else:
            target_name = (targets[0].name if len(targets) == 1
                           else f"{len(targets)} targets")

        actions = {
            Effect.DAMAGE.value: f"Deal {self.cost} damage",
            Effect.HEAL.value: f"Heal {self.cost} health",
            Effect.BUFF.value: f"Buff {self.cost} stats",
            Effect.DEBUFF.value: f"Debuff {self.cost} stats"
        }

        prefix = actions.get(self.effect_type, "Applied effect")
        return {"effect": f"{prefix} to {target_name}"}
