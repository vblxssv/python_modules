from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to summon creature"
            }

    def attack_target(self, target) -> dict:
        damage = self.attack
        target.health -= damage
        if target.health < 0:
            target.health = 0
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
