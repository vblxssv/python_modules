from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity=Rarity.LEGENDARY,
        attack=7,
        health=5
    )

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")

    game_state = {
        "mana": 6
    }

    playable = fire_dragon.is_playable(game_state["mana"])

    print(f"Playable: {playable}")

    result = fire_dragon.play(game_state)

    print(f"Play result: {result}")

    goblin = CreatureCard(
        name="Goblin Warrior",
        cost=2,
        rarity=Rarity.COMMON,
        attack=3,
        health=2
    )

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}")
    print("\nTesting insufficient mana (3 available):")
    low_mana = 3
    playable_low = fire_dragon.is_playable(low_mana)
    print(f"Playable: {playable_low}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
