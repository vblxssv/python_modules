from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    """
    Comprehensive tournament card combining base attributes, 
    combat mechanics, and ranking capabilities.
    """
    def __init__(self, card_id: str, name: str, cost: int, rarity: str, attack_val: int, health_val: int):
        # Initialize base Card class
        super().__init__(name, cost, rarity)
        self.id = card_id
        self.attack_val = attack_val
        self.health = health_val
        self._wins = 0
        self._losses = 0
        self._base_rating = 1200

    # --- Card Interface Implementation ---
    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "status": "success"}
        return {"card_played": self.name, "status": "insufficient_mana"}

    # --- Combatable Interface Implementation ---
    def attack(self, target) -> dict:
        """Executes an attack on a target, returning the result."""
        damage = self.attack_val
        # If the target is Combatable, call its defend method
        if isinstance(target, Combatable):
            return target.defend(damage)
        return {"attacker": self.name, "damage_dealt": damage}

    def defend(self, incoming_damage: int) -> dict:
        """Processes incoming damage as required by Combatable interface."""
        self.health -= incoming_damage
        if self.health < 0:
            self.health = 0
        return {
            "name": self.name, 
            "remaining_health": self.health,
            "incoming_damage": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        """Returns current combat-related attributes."""
        return {
            "attack": self.attack_val,
            "health": self.health
        }

    # --- Rankable Interface Implementation ---
    def calculate_rating(self) -> int:
        """Calculates current rating based on performance."""
        return self._base_rating + (self._wins * 16) - (self._losses * 16)

    def update_wins(self, wins: int) -> None:
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}"
        }

    # --- Tournament-specific Method ---
    def get_tournament_stats(self) -> dict:
        """Returns comprehensive stats for the platform display."""
        return {
            "id": self.id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}"
        }