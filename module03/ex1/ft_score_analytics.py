import sys


def main():
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ..")
        return
    try:
        scores = [int(x) for x in sys.argv[1:]]
        print(F"Scores processed: {scores}")
        print(F"Total players: {len(scores)}")
        print(F"Total score: {sum(scores)}")
        print(F"Average score: {sum(scores) / len(scores)}")
        print(F"High score: {max(scores)}")
        print(F"Low score: {min(scores)}")
        print(F"Score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print(F"Caught ValueError: {e}")


if __name__ == "__main__":
    main()
