from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    A powerful card implementing multiple interfaces.
    Inherits from Card, Combatable, and Magical.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 hp: int = 10, mp: int = 4, atk: int = 5):
        super().__init__(name, cost, rarity)
        self.hp = hp
        self.mana = mp
        self.base_atk = atk
        self.is_alive = True

    def play(self, game_state: dict) -> dict:
        """Implement the abstract play method from Card."""
        return {"action": "play", "card": self.name, "rarity": self.rarity}

    # --- Combat Logic (Combatable) ---
    def attack(self, target: str) -> dict:
        """Perform a melee attack."""
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.base_atk,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        """Process incoming damage with a damage block mechanic."""
        blocked = 3
        actual_damage = max(0, incoming_damage - blocked)
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

        return {
            'defender': self.name,
            'damage_taken': actual_damage,
            'damage_blocked': blocked,
            'still_alive': self.is_alive
        }

    def get_combat_stats(self) -> dict:
        """Get HP and Attack statistics."""
        return {"hp": self.hp, "atk": self.base_atk}

    # --- Magic Logic (Magical) ---
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell by consuming mana."""
        cost_per_target = 2
        total_cost = len(targets) * cost_per_target

        if self.mana >= total_cost:
            self.mana -= total_cost
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': total_cost
            }
        return {"error": "Not enough mana"}

    def channel_mana(self, amount: int) -> dict:
        """Recover mana points."""
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        """Get current mana statistics."""
        return {"mana": self.mana}
