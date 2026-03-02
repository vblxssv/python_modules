from typing import Callable, List, Tuple, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a function that calls two spells and returns a tuple."""
    def combined_spell(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a function with its numerical result multiplied."""
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a function that executes only if condition is met."""
    def cast_if_ready(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_if_ready


def spell_sequence(spells: List[Callable]) -> Callable:
    """Return a function that executes a sequence of spells."""
    def run_sequence(*args: Any, **kwargs: Any) -> List[Any]:
        return [s(*args, **kwargs) for s in spells]
    return run_sequence


# --- Demonstration funcs ---


def fireball(target: str) -> str:
    """Return fireball hit message."""
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    """Return heal message."""
    return f"Heals {target}"


def get_base_damage(target: str) -> int:
    """Return base damage value."""
    return 10


def main():
    """Run higher-order function demonstrations."""
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    multiplier = 3
    mega_fireball = power_amplifier(get_base_damage, multiplier)
    original = get_base_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")


if __name__ == "__main__":
    main()
