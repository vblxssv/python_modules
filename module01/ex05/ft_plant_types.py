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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(F"{self.name} is blooming beatifully!")

    def __repr__(self):
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        return int(3.14159265359 * ((self.trunk_diameter / 10) ** 2))

    def __repr__(self):
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, hgt: int, age: int, season: str, nutr: str):
        super().__init__(name, hgt, age)
        self.harvest_season = season
        self.nutritional_value = nutr

    def __repr__(self):
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")

    def get_benefit(self):
        print(F"{self.name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    lavender = Flower("Lavender", 40, 60, "purple")
    print(rose)
    rose.bloom()
    print(lavender)
    lavender.bloom()
    print("-" * 30)
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 1200, 3650, 80)
    print(oak)
    print(f"{oak.name} provides {oak.produce_shade()} square meters of shade")
    print(pine)
    print(f"{pine.name} provides {pine.produce_shade()} "
          "square meters of shade")
    print("-" * 30)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 120, "autumn", "beta-carotene")
    print(tomato)
    tomato.get_benefit()
    print(carrot)
    carrot.get_benefit()


if __name__ == "__main__":
    main()
