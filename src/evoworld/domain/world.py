import random

from src.evoworld.domain.food import Food
from src.evoworld.domain.creature import Creature
from src.evoworld.config.settings import (
    WORLD_INITIAL_CREATURES,
    WORLD_INITIAL_FOOD,
    WORLD_MAX_FOOD,
    WORLD_WIDTH,
    WORLD_HEIGHT,
)


class World:
    def __init__(self):
        self.width = WORLD_WIDTH
        self.height = WORLD_HEIGHT
        self.food = []
        self.creatures = []

    def spawn_food(self, amount: int = WORLD_INITIAL_FOOD):
        current_food = len(self.food)
        maximum_food_reached = current_food >= WORLD_MAX_FOOD
        if maximum_food_reached:
            return
        aviliable_slots = WORLD_MAX_FOOD - current_food
        spawn_amount = min(amount, aviliable_slots)
        for _ in range(spawn_amount):
            self.food.append(
                Food(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                )
            )

    def spawn_creatures(self, amount: int = WORLD_INITIAL_CREATURES):
        for _ in range(amount):
            self.creatures.append(
                Creature(
                    x=random.randint(0, self.width - 1),
                    y=random.randint(0, self.height - 1),
                )
            )
