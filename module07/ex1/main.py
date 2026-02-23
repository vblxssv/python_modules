from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard, Effect # noqa
from ex0.Card import Rarity


game_state = {"mana": 10, "targets": ["Enemy"]}

spell = SpellCard("Lightning Bolt", 3, Rarity.COMMON, Effect.DAMAGE)

print(spell.play(game_state))
