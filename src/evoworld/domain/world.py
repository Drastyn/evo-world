import random

from src.evoworld.domain.food import Food
from src.evoworld.domain.creature import Creature

_INITIAL_CREATURES = 50
_INITIAL_FOOD = 300
_MAX_FOOD = 600
_WORLD_WIDTH = 100
_WORLD_HEIGHT = 100


class World:
    def __init__(self):
        self.width = _WORLD_WIDTH
        self.height = _WORLD_HEIGHT
        self.food = []
        self.creatures = []

    def spawn_food(self, amount: int = _INITIAL_FOOD, max_food: int = _MAX_FOOD):
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

    def spawn_creatures(self, amount: int = _INITIAL_CREATURES):
        for _ in range(amount):
            self.creatures.append(
                Creature(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                )
            )
