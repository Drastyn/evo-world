import random

_INITIAL_CREATURE_ENERGY = 100
_INITIAL_CREATURE_COLOR = (255, 255, 255)
_REPRODUCTION_ENERGY = 200
_ENERGY_COST_MOVE = 1


class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = _INITIAL_CREATURE_ENERGY
        self.color = _INITIAL_CREATURE_COLOR

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.energy -= _ENERGY_COST_MOVE

    def eat(self, food):
        eat_condition = self.x == food.x and self.y == food.y
        if eat_condition:
            self.energy += food.energy
            return True
        return False

    def reproduce(self):
        if self.energy >= _REPRODUCTION_ENERGY:
            self.energy //= 2
            return Creature(x=self.x, y=self.y)
        return None
