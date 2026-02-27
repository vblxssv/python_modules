import functools
import operator

# Инициализация артефакта свертки
def spell_reducer(spells: list[int], operation: str) -> int:
    """Комбинирует силы заклинаний, используя functools.reduce."""
    # Словарь сопоставления строк и функций из модуля operator
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(ops[operation], spells)

# Базовая функция для частичного применения
def base_enchantment(power, element, target):
    return f"Enchanted {target} with {element} (Power: {power})"

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Создает специализированные версии функции через functools.partial."""
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, "Fire"),
        'ice_enchant': functools.partial(base_enchantment, 50, "Ice"),
        'lightning_enchant': functools.partial(base_enchantment, 50, "Lightning")
    }

# Артефакт кэширования (мемоизации)
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Вычисляет число Фибоначчи с использованием кэша."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

# Артефакт множественной диспетчеризации
def spell_dispatcher() -> callable:
    """Создает систему обработки заклинаний на основе типов данных."""
    @functools.singledispatch
    def dispatcher(spell):
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(damage):
        return f"Direct Damage Spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment):
        return f"Applied Enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast):
        return f"Multi-casting: {', '.join(map(str, multi_cast))}"

    return dispatcher

def main():
    # 1. Тестирование spell_reducer
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    # 2. Тестирование memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    
    # 3. Демонстрация dispatcher (опционально, для полноты)
    dispatch = spell_dispatcher()
    # print(dispatch(100))
    # print(dispatch("Shield"))

if __name__ == "__main__":
    main()