from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

def main():
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")
    
    deck = Deck()
    
    spell = SpellCard("Lightning Bolt", 3, Rarity.COMMON, Effect.DAMAGE.value)
    artifact = ArtifactCard("Mana Crystal", 2, Rarity.RARE, 5, "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 7, Rarity.EPIC, 5, 10)
    
    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)
    
    # Вывод статов
    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")
    
    print("\nDrawing and playing cards:")
    
    # game_state с пустой целью, чтобы сработал "target" в заклинании
    game_state = {"mana": 10, "targets": []}
    
    # 1. Spell
    drawn_1 = deck.draw_card()
    print(f"Drew: {drawn_1.name} (Spell)")
    res_1 = drawn_1.play(game_state)
    print(f"Play result: {{'card_played': '{res_1['card_played']}'\n,\n'mana_used': {res_1['mana_used']},\n'effect': '{res_1['effect']}'}}")
    
    # 2. Artifact
    drawn_2 = deck.draw_card()
    print(f"Drew: {drawn_2.name} (Artifact)")
    res_2 = drawn_2.play(game_state)
    print(f"Play result: {{'card_played': '{res_2['card_played']}'\n,\n'mana_used': {res_2['mana_used']},\n'effect': '{res_2['effect']}'}}")
    
    # 3. Creature
    drawn_3 = deck.draw_card()
    print(f"Drew: {drawn_3.name} (Creature)")
    # Для примера мана должна быть 5
    drawn_3.cost = 5
    res_3 = drawn_3.play(game_state)
    print(f"Play result: {{'card_played': '{res_3['card_played']}'\n,\n'mana_used': {res_3['mana_used']},\n'effect': '{res_3['effect']}'}}")
    
    print("\nPolymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()