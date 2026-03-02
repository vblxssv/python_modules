from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Management system for registering cards and running matches."""

    def __init__(self):
        self._registry: Dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Add a card to the tournament roster."""
        self._registry[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards based on attack power."""
        c1 = self._registry[card1_id]
        c2 = self._registry[card2_id]

        if c1.attack_val >= c2.attack_val:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self._matches_played += 1

        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[TournamentCard]:
        """Return cards sorted by rating in descending order."""
        return sorted(
            self._registry.values(),
            key=lambda x: x.calculate_rating(),
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        """Provide a summary of platform activity."""
        ratings = [c.calculate_rating() for c in self._registry.values()]
        avg = sum(ratings) / len(ratings) if ratings else 0
        return {
            'total_cards': len(self._registry),
            'matches_played': self._matches_played,
            'avg_rating': int(avg),
            'platform_status': 'active'
        }
