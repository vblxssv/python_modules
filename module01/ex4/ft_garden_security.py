class SecurePlant:
    def __init__(self, name: str):
        self._name = name
        self._height = 0
        self._age = 0
        print(F"Plant created: {name}")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new: int) -> None:
        if new < 0:
            print(F"Invalid operation attempted: height {new}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new
            print(F"Height updated: {new}cm [OK]")

    def set_age(self, new: int) -> None:
        if new < 0:
            print(F"Invalid operation attempted: age {new} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new
            print(F"Age updated: {new} days [OK]")

    def __repr__(self):
        return F"{self._name} ({self._height}cm, {self._age} days)"


def main():
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(F"Current plant: {rose}")


if __name__ == "__main__":
    main()
