import random
from src.evoworld.config.settings import (
    CREATURE_INITIAL_ENERGY,
    CREATURE_INITIAL_COLOR,
    CREATURE_REPRODUCTION_ENERGY,
    CREATURE_MOVE_ENERGY_COST,
    CREATURE_HUNGRY_LEVELS,
)


class Creature:
    _hungry_levels = sorted(CREATURE_HUNGRY_LEVELS.keys(), reverse=True)

    def __init__(self, x, y, genome):
        self.x = x
        self.y = y
        self.energy = CREATURE_INITIAL_ENERGY
        self.color = CREATURE_INITIAL_COLOR
        self.genome = genome

    def find_nearest_food(self, foods):
        visible_foods = []
        for food in foods:
            distance = abs(food.x - self.x) + abs(food.y - self.y)
            if distance < -self.genome.vision:
                visible_foods.append(distance, food)
        if not visible_foods:
            return None
        visible_foods.sort(key=lambda x: x[0])
        return visible_foods[0][1]

    def move_random(self, width, height):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x %= width
        self.y %= height
        self.energy -= CREATURE_MOVE_ENERGY_COST

    def move_towards(self, target):
        if target.x > self.x:
            self.x += 1
        elif target.x < self.x:
            self.x -= 1
        if target.y > self.y:
            self.y += 1
        elif target.y < self.y:
            self.y -= 1

    def hungry(self, hungry_level):
        threshold = max(level for level in self._hungry_levels if hungry_level >= level)
        self.color = CREATURE_HUNGRY_LEVELS[threshold]

    def eat(self, food):
        eat_condition = self.x == food.x and self.y == food.y
        if eat_condition:
            self.energy += food.energy
        return eat_condition

    def reproduce(self):
        if self.energy >= CREATURE_REPRODUCTION_ENERGY:
            self.energy //= 2
            return Creature(x=self.x, y=self.y, genome=self.genome.mutate())
        return None

    def death(self):
        death_condition = self.energy <= 0
        return death_condition
