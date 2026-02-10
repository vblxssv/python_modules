class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(F"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, status: str):
        super().__init__(name, height)
        self.color = color
        self.status = status


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, status: str):
        super().__init__(name, height, color, status)
        self.points = 0


class GardenManager:
    def __init__(self):
        self.gardens = {}

    def add_plant(self, owner: str, plant: Plant) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        print(F"Added {plant.name} to {owner}'s garden")

    class GardenStats:
        pass
    pass
