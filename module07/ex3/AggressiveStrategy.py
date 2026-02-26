from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    """
    Concrete strategy: Aggressive.
    Focuses on low-cost cards, maximum damage, and face-targeting.
    """

    def get_strategy_name(self) -> str:
        """Returns the identifier of the strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Dict]) -> List[Dict]:
        """
        Prioritizes targets: Enemy Player first, then lowest health creatures.
        In Aggressive mode, 'Face is the place'.
        """
        # Sort targets: 'Player' always comes first, then by health ascending
        return sorted(
            available_targets, 
            key=lambda t: (0 if t.get("type") == "Player" else 1, t.get("health", 0))
        )

    def execute_turn(self, hand: List[Card], battlefield: List[CreatureCard]) -> Dict[str, Any]:
        """
        Simulates turn execution: 
        1. Plays low-cost cards from hand.
        2. Attacks with creatures already on the battlefield.
        """
        game_state = {"mana": 10} # Context mana for the turn simulation
        cards_played = []
        mana_start = game_state["mana"]
        
        # --- PHASE 1: Playing Cards ---
        # Sort hand: Low cost first for board presence
        playable_in_order = sorted(
            [c for c in hand if c.is_playable(game_state["mana"])],
            key=lambda c: c.cost
        )

        for card in playable_in_order:
            if card.is_playable(game_state["mana"]):
                card.play(game_state)
                cards_played.append(card.name)
            else:
                break

        # --- PHASE 2: Attacking ---
        # In a real game, battlefield would contain CreatureCard instances
        total_damage = sum(getattr(c, 'attack', 0) for c in battlefield)
        
        # Define available targets for prioritization
        targets = [{"name": "Enemy Player", "type": "Player", "health": 30}]
        prioritized = self.prioritize_targets(targets)

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_start - game_state["mana"],
            "targets_attacked": [t["name"] for t in prioritized],
            "damage_dealt": total_damage + sum(getattr(c, 'attack', 0) for c in hand if c.name in cards_played and isinstance(c, CreatureCard)),
            "combat_resolved": True
        }