import functools
import operator
from typing import List, Dict, Callable, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduce spell powers using functools.reduce and operator functions."""
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    """Apply a base enchantment with power, element, and target."""
    return f"Enchanted {target} with {element} (Power: {power})"


def partial_enchanter(
    base_func: Callable[[int, str, str], str]
) -> Dict[str, Callable[[str], str]]:
    """Create specialized partial applications of the base enchantment."""
    return {
        'fire_enchant': functools.partial(base_func, 50, "Fire"),
        'ice_enchant': functools.partial(base_func, 50, "Ice"),
        'lightning_enchant': functools.partial(base_func, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate Fibonacci number with LRU caching for optimization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single-dispatch system to handle different spell types."""
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"Direct Damage Spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"Applied Enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast: list) -> str:
        return f"Multi-casting: {', '.join(map(str, multi_cast))}"

    return dispatcher


def main():
    """Execute demonstration of functools artifacts."""
    # 1. Testing spell_reducer
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    # 2. Testing memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    # 3. Demonstration of dispatcher
    # dispatch = spell_dispatcher()
    # print(dispatch(100))
    # print(dispatch("Shield"))


if __name__ == "__main__":
    main()
