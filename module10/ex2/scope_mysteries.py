from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Create a counter closure that increments on each call."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create a power accumulator starting from initial_power."""
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a function that applies a specific enchantment to an item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Create a private memory storage system with store and recall."""
    vault: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    """Demonstrate lexical scoping and closures."""
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))


if __name__ == "__main__":
    main()
