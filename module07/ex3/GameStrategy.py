from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract interface for game execution strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Process turn logic based on current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Determine target priority based on strategy logic."""
        pass
