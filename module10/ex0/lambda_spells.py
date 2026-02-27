# lambda_spells.py

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    # Сортировка по 'power' в порядке убывания (reverse=True)
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    # Фильтрация магов, чья сила >= min_power
    return list(filter(lambda m: m['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    # Добавление префикса "* " и суффикса " *" к именам заклинаний
    return list(map(lambda s: f"* {s} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    # Извлечение списка только уровней силы для расчетов
    powers = list(map(lambda m: m['power'], mages))
    
    if not powers:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    # Использование лямбда-выражений (как ключей или для вычислений)
    return {
        'max_power': max(powers, key=lambda p: p),
        'min_power': min(powers, key=lambda p: p),
        'avg_power': round(sum(powers) / len(powers), 2)
    }

def main():
    # Данные для тестирования
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Wooden Shield', 'power': 40, 'type': 'armor'}
    ]
    
    spells = ["fireball", "heal", "shield"]
    
    mages = [
        {'name': 'Merlin', 'power': 95, 'element': 'arcane'},
        {'name': 'Morgana', 'power': 88, 'element': 'shadow'},
        {'name': 'Novice', 'power': 30, 'element': 'earth'}
    ]

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    if len(sorted_arts) >= 2:
        print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
              f"comes before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

if __name__ == "__main__":
    main()