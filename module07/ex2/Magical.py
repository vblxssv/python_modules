from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface for magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Execute a magical spell on a list of targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Increase current mana capacity."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return current mana status."""
        pass
