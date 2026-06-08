import random

from src.evoworld.domain.food import Food
from src.evoworld.domain.creature import Creature


class World:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.food = []
        self.creatures = []

    def spawn_food(self, amount: int):
        for _ in range(amount):
            self.food.append(
                Food(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                )
            )

    def spawn_creatures(self, amount: int):
        for _ in range(amount):
            self.creatures.append(
                Creature(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                    energy=75,
                )
            )
