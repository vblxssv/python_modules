import random
import time
from typing import Generator


def game_events(num_events: int) -> Generator[str, None, None]:
    players = ['alice', 'bob', 'charlie']
    actions = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, num_events + 1):
        player = random.choice(players)
        action = random.choice(actions)
        level = random.randint(1, 20)
        yield f"Event {i}: Player {player} (level {level}) {action}"


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def primes(n: int) -> Generator[int, None, None]:
    count, candidate = 0, 2
    while count < n:
        if is_prime(candidate):
            yield candidate
            count += 1
        candidate += 1


def main():
    print("=== Game Data Stream Processor ===")
    num_events = 1000
    print(f"Processing {num_events} game events...")

    event_generator = game_events(num_events)

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    start_time = time.time()
    for event in event_generator:
        total_events += 1
        print(event)
        level = int(event.split('level ')[1].split(')')[0])
        if level >= 10:
            high_level += 1
        if 'found treasure' in event:
            treasure_events += 1
        if 'leveled up' in event:
            level_up_events += 1
    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    # === Демонстрация генераторов ===
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", ", ".join(str(n)
                                                      for n in fibonacci(10)))
    print("Prime numbers (first 5):", ", ".join(str(p) for p in primes(5)))


if __name__ == "__main__":
    main()
