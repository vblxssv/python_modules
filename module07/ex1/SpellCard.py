from ex0.Card import Card
from ex1.ArtifactCard import Effect


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        current_mana = game_state.get("mana", 0)
        if current_mana < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        game_state["mana"] -= self.cost
        targets = game_state.get("targets", [])
        hand = game_state.get("hand", [])
        if self in hand:
            hand.remove(self)
        effect_data = self.resolve_effect(targets)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_data["effect"]
        }

    def resolve_effect(self, targets: list) -> dict:
        if not targets:
            target_name = "target"
        else:
            target_name = targets[0].name if len(targets) == 1 else f"{len(targets)} targets" # noqa
        actions = {
            Effect.DAMAGE.value: f"Deal {self.cost} damage",
            Effect.HEAL.value: f"Heal {self.cost} health",
            Effect.BUFF.value: f"Buff {self.cost} stats",
            Effect.DEBUFF.value: f"Debuff {self.cost} stats"
        }

        for target_obj in targets:
            if self.effect_type == Effect.DAMAGE.value:
                target_obj.health -= self.cost
            elif self.effect_type == Effect.HEAL.value:
                target_obj.health += self.cost
            elif self.effect_type == Effect.BUFF.value:
                target_obj.attack += self.cost
            elif self.effect_type == Effect.DEBUFF.value:
                target_obj.attack -= self.cost

        prefix = actions.get(self.effect_type, "Applied effect")
        return {"effect": f"{prefix} to {target_name}"}
