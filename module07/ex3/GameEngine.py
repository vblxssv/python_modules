from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates interactions between factory and strategy."""

    def __init__(self):
        self._factory = None
        self._strategy = None
        self._turns_simulated = 0
        self._total_damage = 0
        self._total_cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Set factory and strategy and print configuration."""
        self._factory = factory
        self._strategy = strategy
        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        """Run a turn simulation using factory and strategy."""
        deck_data = self._factory.create_themed_deck(size=3)
        hand = deck_data["deck"]
        self._total_cards_created += len(hand)

        hand_display = [f"{c.name} ({c.cost})" for c in hand]
        print("Simulating aggressive turn...")
        print(f"Hand: [{', '.join(hand_display)}]")

        turn_results = self._strategy.execute_turn(hand, [])
        self._turns_simulated += 1
        self._total_damage += turn_results.get("damage_dealt", 0)
        return turn_results

    def get_engine_status(self) -> dict:
        """Return summary of the simulation."""
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': self._strategy.get_strategy_name(),
            'total_damage': self._total_damage,
            'cards_created': self._total_cards_created
        }
