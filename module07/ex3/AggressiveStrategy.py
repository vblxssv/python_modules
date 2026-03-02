from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    """Concrete aggressive strategy: prioritizes damage and low-cost plays."""

    def get_strategy_name(self) -> str:
        """Return identifier."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Dict]) -> List[Dict]:
        """Prioritize Player first, then targets by health ascending."""
        return sorted(
            available_targets,
            key=lambda t: (0 if t.get("type") == "Player" else 1,
                           t.get("health", 0))
        )

    def execute_turn(self, hand: List[Card],
                     battlefield: List[CreatureCard]) -> Dict[str, Any]:
        """Execute turn by playing low-cost cards and attacking."""
        game_state = {"mana": 10}
        cards_played = []
        mana_start = game_state["mana"]

        # Sort hand: Low cost first
        playable = sorted(
            [c for c in hand if c.is_playable(game_state["mana"])],
            key=lambda c: c.cost
        )

        for card in playable:
            if card.is_playable(game_state["mana"]):
                card.play(game_state)
                cards_played.append(card.name)

        # Attacking logic
        total_dmg = sum(getattr(c, 'attack', 0) for c in battlefield)
        total_dmg += sum(getattr(c, 'attack', 0) for c in hand
                         if c.name in cards_played
                         and isinstance(c, CreatureCard))

        targets = [{"name": "Enemy Player", "type": "Player", "health": 30}]
        prioritized = self.prioritize_targets(targets)

        return {
            "cards_played": cards_played,
            "mana_used": mana_start - game_state["mana"],
            "targets_attacked": [t["name"] for t in prioritized],
            "damage_dealt": total_dmg
        }
