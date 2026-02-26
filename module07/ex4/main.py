from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 8, 8)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Rare", 5, 4)

    for card in [dragon, wizard]:
        platform.register_card(card)
        stats = card.get_tournament_stats()
        print(f"{card.name} (ID: {card.id}):")
        print(f"- Interfaces: {stats['interfaces']}")
        print(f"- Rating: {stats['rating']}")
        print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        info = card.get_rank_info()
        print(f"{i}. {card.name} - Rating: {info['rating']} ({info['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()