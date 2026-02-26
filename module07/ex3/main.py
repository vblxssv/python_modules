from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

def main():
    print("=== DataDeck Game Engine ===")
    
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)
    
    results = engine.simulate_turn()
    
    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {results}")

    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()