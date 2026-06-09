from evoworld.config.settings import FOOD_ENERGY


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = FOOD_ENERGY
