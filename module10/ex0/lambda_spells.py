from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """Sort artifacts by power descending."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """Filter mages by minimum power level."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Add decorative stars to spell names."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    """Calculate power statistics for mages."""
    powers = list(map(lambda m: m['power'], mages))
    if not powers:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2)
    }


def main():
    """Execute demonstration of lambda spells."""
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Wooden Shield', 'power': 40, 'type': 'armor'}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    if len(sorted_arts) >= 2:
        # Разбиваем длинную строку для соответствия лимиту 79/88 символов
        first = f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power)"
        second = f"{sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)"
        print(f"{first} comes before {second}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
