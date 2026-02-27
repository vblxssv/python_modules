
def mage_counter() -> callable:
    """Создает счетчик, который увеличивается при каждом вызове."""
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> callable:
    """Создает сумматор магической силы."""
    total_power = initial_power
    def accumulator(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator

def enchantment_factory(enchantment_type: str) -> callable:
    """Создает функции для зачарования предметов."""
    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchant

def memory_vault() -> dict[str, callable]:
    """Создает систему приватного хранилища памяти."""
    vault = {}
    
    def store(key: str, value):
        vault[key] = value
        
    def recall(key: str):
        return vault.get(key, "Memory not found")
        
    return {"store": store, "recall": recall}

def main():
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