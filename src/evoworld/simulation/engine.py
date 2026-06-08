import random

from src.evoworld.domain.creature import Creature


class Engine:
    def __init__(self, world, config):
        self.world = world
        self.config = config

    def tick(self):
        newborns = []
        for creature in self.world.creatures[:]:
            creature.move()
            creature.energy -= self.config.ENERGY_COST_MOVE
            creature.x %= self.world.width
            creature.y %= self.world.height
            for food in self.world.food[:]:
                eaten = creature.x == food.x and creature.y == food.y
                if eaten:
                    creature.energy += self.config.ENERGY_FROM_FOOD
                    self.world.food.remove(food)
                    break
            if creature.energy <= 0:
                self.world.creatures.remove(creature)
                continue
            if creature.energy >= self.config.REPRODUCTION_ENERGY:
                creature.energy //= 2
                newborn = Creature(
                    x=creature.x,
                    y=creature.y,
                    energy=creature.energy,
                    config=self.config,
                )
                newborns.append(newborn)
        self.world.creatures.extend(newborns)
        self.world.spawn_food(1, self.config.MAX_FOOD)
