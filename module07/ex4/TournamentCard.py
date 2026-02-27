from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Advanced card type for tournament play.
    Implements Card, Combatable, and Rankable interfaces.
    """

    def __init__(self, card_id: str, name: str, cost: int,
                 rarity: str, attack_val: int, health_val: int):
        super().__init__(name, cost, rarity)
        self.id = card_id
        self.attack_val = attack_val
        self.health = health_val
        self._wins = 0
        self._losses = 0
        self._base_rating = 1200

    def play(self, game_state: dict) -> dict:
        """Process playing the card in a tournament match."""
        if self.is_playable(game_state.get("mana", 0)):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "status": "success"}
        return {"card_played": self.name, "status": "insufficient_mana"}

    def attack(self, target) -> dict:
        """Execute combat attack on a target."""
        damage = self.attack_val
        if isinstance(target, Combatable):
            return target.defend(damage)
        return {"attacker": self.name, "damage_dealt": damage}

    def defend(self, incoming_damage: int) -> dict:
        """Handle incoming combat damage."""
        self.health = max(0, self.health - incoming_damage)
        return {
            "name": self.name,
            "remaining_health": self.health,
            "incoming_damage": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        """Return current combat attributes."""
        return {"attack": self.attack_val, "health": self.health}

    def calculate_rating(self) -> int:
        """Elo calculation: base + (wins * 16) - (losses * 16)."""
        return self._base_rating + (self._wins * 16) - (self._losses * 16)

    def update_wins(self, wins: int) -> None:
        """Record tournament wins."""
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        """Record tournament losses."""
        self._losses += losses

    def get_rank_info(self) -> dict:
        """Return ranking summary."""
        return {
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}"
        }

    def get_tournament_stats(self) -> dict:
        """Return comprehensive performance data."""
        return {
            "id": self.id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": self.calculate_rating(),
            "record": f"{self._wins}-{self._losses}"
        }
