from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface for combat capabilities."""

    @abstractmethod
    def attack(self, target: str) -> dict:
        """Execute an attack on a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Handle incoming damage logic."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return current health and attack power."""
        pass
