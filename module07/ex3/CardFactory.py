from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed card sets."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Generate a collection of themed cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return dictionary of supported card names/types."""
        pass
