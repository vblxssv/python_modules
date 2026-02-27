import functools
import time
import re
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Decorator factory that validates the power level of a spell."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Check for 'power' in kwargs or specific positions in args
            # For cast_spell(self, spell_name, power), power is args[2]
            pwr = kwargs.get('power')
            if pwr is None:
                if len(args) > 2:  # Method call: (self, name, power)
                    pwr = args[2]
                elif len(args) > 0:  # Direct call: (power, ...)
                    pwr = args[0]

            if pwr is not None and pwr >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """Decorator that retries a function call upon exception."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Class representing a guild of mages with spell-casting logic."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate name: min 3 chars, letters and spaces only."""
        if len(name) < 3:
            return False
        return bool(re.fullmatch(r"[A-Za-z\s]+", name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power level is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


# --- Demonstration funcs ---


@spell_timer
def fireball() -> str:
    """Simulate a long fireball cast."""
    time.sleep(0.1)
    return "Fireball cast!"


def main():
    """Run demonstrations for decorators and class methods."""
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    guild = MageGuild()

    # Test staticmethod
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("G2"))

    # Test power_validator
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))


if __name__ == "__main__":
    main()
