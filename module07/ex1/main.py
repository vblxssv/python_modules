from ex0.main import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    """Demonstrate deck building and polymorphic card behavior."""
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    spell = SpellCard("Lightning Bolt", 3, Rarity.COMMON.value,
                      Effect.DAMAGE.value)
    artifact = ArtifactCard("Mana Crystal", 2, Rarity.RARE.value,
                            5, "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, Rarity.EPIC.value, 7, 5)

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")

    game_state = {"mana": 10, "targets": []}

    # Play Spell
    drawn = deck.draw_card()
    print(f"Drew: {drawn.name} (Spell)")
    print(f"Play result: {drawn.play(game_state)}")

    # Play Artifact
    drawn = deck.draw_card()
    print(f"Drew: {drawn.name} (Artifact)")
    print(f"Play result: {drawn.play(game_state)}")

    # Play Creature
    drawn = deck.draw_card()
    print(f"Drew: {drawn.name} (Creature)")
    print(f"Play result: {drawn.play(game_state)}")

    print("\nPolymorphism in action: Same interface, different behavior!")


if __name__ == "__main__":
    main()
