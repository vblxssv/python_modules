from typing import Dict, Any, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    The orchestrator that manages the interaction between the 
    Abstract Factory (Card Creation) and the Strategy (Gameplay Logic).
    """

    def __init__(self):
        self._factory: CardFactory = None
        self._strategy: GameStrategy = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._total_cards_created: int = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """Configures the engine with a concrete factory and strategy."""
        self._factory = factory
        self._strategy = strategy
        
        # Display configuration info as per expected output
        factory_name = factory.__class__.__name__
        theme_name = factory_name.replace('CardFactory', '')
        
        print(f"Configuring {theme_name} Card Game...")
        print(f"Factory: {factory_name}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {self._factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        """
        Executes a single game turn: 
        1. Generates cards using the factory.
        2. Applies strategy to the hand.
        """
        if not self._factory or not self._strategy:
            raise RuntimeError("Engine must be configured before simulating a turn.")

        # 1. Create a hand (themed deck/collection of cards)
        # We simulate a hand of 3 cards for the turn
        deck_data = self._factory.create_themed_deck(size=3)
        hand = deck_data["deck"]
        self._total_cards_created += len(hand)

        # Format hand for display: Name (Value/Cost)
        hand_display = [f"{c.name} ({c.cost})" for c in hand]
        
        print(f"Simulating {self._strategy.get_strategy_name().lower().replace('strategy', '')} turn...")
        print(f"Hand: [{', '.join(hand_display)}]")

        # 2. Execute turn using the Strategy Pattern
        # Battlefield is empty for the first simulated turn
        turn_execution = self._strategy.execute_turn(hand, battlefield=[])
        
        # Update internal statistics
        self._turns_simulated += 1
        self._total_damage += turn_execution.get("damage_dealt", 0)

        return turn_execution

    def get_engine_status(self) -> dict:
        """Returns a summary of the game simulation."""
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': self._strategy.get_strategy_name() if self._strategy else None,
            'total_damage': self._total_damage,
            'cards_created': self._total_cards_created
        }