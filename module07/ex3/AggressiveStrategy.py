from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Executes aggressive turn:
        - Plays lowest-cost creatures first
        - Attacks with all creatures
        - Prioritizes enemy creatures, then player
        """

        turn_result = {
            "strategy": self.get_strategy_name(),
            "cards_played": [],
            "attacks": [],
            "mana_remaining": 0,
            "battlefield_state": [],
            "summary": ""
        }

        game_state = {
            "mana": self.available_mana,
            "battlefield": battlefield,
            "enemy_battlefield": self.enemy_battlefield,
            "enemy_player": self.enemy_player
        }

        creatures_in_hand = [
            card for card in hand if isinstance(card, CreatureCard)
        ]

        creatures_in_hand.sort(key=lambda c: c.cost)

        for creature in creatures_in_hand:
            if creature.cost <= game_state["mana"]:
                result = creature.play(game_state)

                if result["mana_used"] > 0:
                    battlefield.append(creature)
                    turn_result["cards_played"].append(result)
        targets = self.prioritize_targets(
            self.enemy_battlefield + [self.enemy_player]
        )

        for creature in battlefield:

            if creature.health <= 0:
                continue

            if not targets:
                break

            target = targets[0]

            attack_result = creature.attack_target(target)
            turn_result["attacks"].append(attack_result)

            # Remove dead creature targets
            if hasattr(target, "health") and target.health <= 0:
                if target in self.enemy_battlefield:
                    self.enemy_battlefield.remove(target)
                targets = self.prioritize_targets(
                    self.enemy_battlefield + [self.enemy_player]
                )

        # 3. Final state
        turn_result["mana_remaining"] = game_state["mana"]

        turn_result["battlefield_state"] = [
            creature.get_card_info() for creature in battlefield
        ]

        # 4. Summary
        turn_result["summary"] = (
            f"Aggressive turn complete: "
            f"{len(turn_result['cards_played'])} creatures played, "
            f"{len(turn_result['attacks'])} attacks executed."
        )

        return turn_result


    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"


    def prioritize_targets(self, available_targets: list) -> list:
        """
        Priority:
        1. Enemy creatures with lowest health (easy kills)
        2. Enemy player last
        """

        creatures = [
            target for target in available_targets
            if isinstance(target, CreatureCard)
        ]

        player = [
            target for target in available_targets
            if not isinstance(target, CreatureCard)
        ]

        creatures.sort(key=lambda c: c.health)

        return creatures + player