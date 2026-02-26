from typing import List, Dict
from ex4.TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):
        self._registry: Dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self._registry[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self._registry[card1_id]
        c2 = self._registry[card2_id]
        
        # Симуляция боя: у кого атака больше, тот и выиграл
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

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._registry.values(), 
            key=lambda x: x.calculate_rating(), 
            reverse=True
        )
        return sorted_cards

    def generate_tournament_report(self) -> dict:
        ratings = [c.calculate_rating() for c in self._registry.values()]
        avg = sum(ratings) / len(ratings) if ratings else 0
        return {
            'total_cards': len(self._registry),
            'matches_played': self._matches_played,
            'avg_rating': avg,
            'platform_status': 'active'
        }
