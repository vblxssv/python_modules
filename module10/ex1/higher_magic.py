from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a function that calls two spells and returns a tuple."""
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
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


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that executes a sequence of spells."""
    def run_sequence(*args: Any, **kwargs: Any) -> list[Any]:
        return [s(*args, **kwargs) for s in spells]

    return run_sequence


def fireball(target: str, *args: Any, **kwargs: Any) -> str:
    """Return fireball hit message"""
    return f"Fireball hits {target}"


def heal(target: str, *args: Any, **kwargs: Any) -> str:
    """Return heal message"""
    return f"Heals {target}"


def get_base_damage() -> int:
    """Return base damage value."""
    return 10


def ice_blast(target: str) -> str:
    """Return ice blast hit message."""
    return f"Ice blast hits {target}"


def check_mana(target: str, mana: int) -> bool:
    """Check if there is enough mana to cast a spell."""
    return mana > 50


def main():
    """Run higher-order function demonstrations."""
    # 1. Spell Combiner
    print("--- Testing spell combiner ---")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    # 2. Power Amplifier
    print("\n--- Testing power amplifier ---")
    mega_fireball = power_amplifier(get_base_damage, 3)
    original = get_base_damage()
    amplified = mega_fireball()
    print(f"Original: {original}, Amplified: {amplified}")

    # 3. Conditional Caster
    print("\n--- Testing conditional caster ---")
    safe_fireball = conditional_caster(check_mana, fireball)

    print(f"Enough mana (80): {safe_fireball('Goblin', 80)}")
    print(f"Low mana (20):    {safe_fireball('Goblin', 20)}")

    # 4. Spell Sequence
    print("\n--- Testing spell sequence ---")
    grimoire = [fireball, heal, ice_blast]
    combo = spell_sequence(grimoire)

    results = combo("Hydra")
    print("Executing sequence:")
    for i, res in enumerate(results, 1):
        print(f"  Step {i}: {res}")


if __name__ == "__main__":
    main()
