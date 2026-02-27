# higher_magic.py

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Возвращает функцию, которая вызывает оба заклинания и возвращает кортеж результатов."""
    def combined_spell(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Возвращает функцию, результат которой умножен на множитель."""
    def amplified_spell(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell

def conditional_caster(condition: callable, spell: callable) -> callable:
    """Возвращает функцию, которая срабатывает только при выполнении условия."""
    def cast_if_ready(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_if_ready

def spell_sequence(spells: list[callable]) -> callable:
    """Возвращает функцию, которая последовательно вызывает список заклинаний."""
    def run_sequence(*args, **kwargs):
        return [s(*args, **kwargs) for s in spells]
    return run_sequence

# --- Функции для демонстрации ---

def fireball(target):
    return f"Fireball hits {target}"

def heal(target):
    return f"Heals {target}"

def get_base_damage(target):
    return 10

def main():
    # Тестирование spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    # Тестирование power_amplifier
    print("\nTesting power amplifier...")
    multiplier = 3
    mega_fireball = power_amplifier(get_base_damage, multiplier)
    original = get_base_damage("Dragon")
    amplified = mega_fireball("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")

if __name__ == "__main__":
    main()