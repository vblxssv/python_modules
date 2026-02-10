class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(F"Created: {name} ({height}cm, {age} days)")

    def __repr__(self):
        return F"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    def get_info(self):
        print(self)


def main():
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    garden = [Plant(*data) for data in plant_data]
    print(F"Total plants created: {len(garden)}")


if __name__ == "__main__":
    main()
