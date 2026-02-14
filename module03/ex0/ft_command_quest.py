import sys


def main():
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(F"Arguments received: {len(sys.argv) - 1}")
        for arg in range(1, len(sys.argv)):
            print(F"Argument {arg}: {sys.argv[arg]}")
    print(F"Program name: {sys.argv[0]}")
    print(F"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
