import random

from src.evoworld.domain.food import Food
from src.evoworld.domain.creature import Creature


class World:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.food = []
        self.creatures = []

    def spawn_food(self, amount: int, max_food: int = None):
        current_food = len(self.food)
        maximum_food_reached = max_food is not None and current_food >= max_food
        if maximum_food_reached:
            return
        aviliable_slots = max_food - current_food if max_food else amount
        spawn_amount = min(amount, aviliable_slots)
        for _ in range(spawn_amount):
            self.food.append(
                Food(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                )
            )

    def spawn_creatures(self, amount: int, energy: int):
        for _ in range(amount):
            self.creatures.append(
                Creature(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                    energy=energy,
                )
            )
