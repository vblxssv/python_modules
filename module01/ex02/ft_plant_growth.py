class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self):
        return F"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    def get_info(self):
        print(self)


def main():
    rose = Plant("Rose", 25, 30)
    start_height = rose.height
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(6):
        rose.grow()
        rose.age_up()
    print("=== Day 7 ===")
    rose.get_info()
    print(F"Growth this week: +{rose.height - start_height}cm")


if __name__ == "__main__":
    main()
