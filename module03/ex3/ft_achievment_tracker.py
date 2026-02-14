

def main():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print(F"Player alice achievments: {alice}")
    print(F"Player bob achievments: {bob}")
    print(F"Player charlie achievments: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievments: {unique}")
    print(F"Total unique achievments: {len(unique)}\n")
    common = alice.intersection(bob, charlie)

    print(f"Common to all players: {common}")
    rare = alice.difference(bob, charlie).union(bob.difference(alice, charlie),
                                                charlie.difference(alice, bob))
    print(F"Rare achievments (1 player): {rare}\n")
    alice_vs_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_vs_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
