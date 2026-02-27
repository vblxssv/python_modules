from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for ranking and performance tracking."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current Elo-style rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increment the win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increment the loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a dictionary with rating and win-loss record."""
        pass
