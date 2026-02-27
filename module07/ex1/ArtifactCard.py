from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete implementation of an artifact card for permanent effects."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Place the artifact into the active game state."""
        current_mana = game_state.get("mana", 0)
        if not self.is_playable(current_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        game_state["mana"] -= self.cost
        if "active_artifacts" not in game_state:
            game_state["active_artifacts"] = []
        game_state["active_artifacts"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> dict:
        """Trigger the artifact's special ability, reducing durability."""
        if self.durability <= 0:
            return {"effect": "Artifact is broken"}
        self.durability -= 1
        return {
            "effect": self.effect,
            "remaining_durability": self.durability
        }
