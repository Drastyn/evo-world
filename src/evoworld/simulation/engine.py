import random


class Engine:
    def __init__(self, world):
        self.world = world

    def tick(self):
        newborns = []
        for creature in self.world.creatures[:]:
            self._move_creature(creature)
            self._energy_ratio(creature)
            for food in self.world.food[:]:
                if creature.eat(food):
                    self.world.food.remove(food)
                    break
            if creature.energy <= 0:
                self.world.creatures.remove(creature)
                continue
            self._reproduce_creature(creature, newborns)
        self.world.creatures.extend(newborns)
        self.world.spawn_food(
            max(1, len(self.world.creatures) // 5),
        )

    def _move_creature(self, creature):
        creature.move()
        creature.x %= self.world.width
        creature.y %= self.world.height

    def _energy_ratio(self, creature):
        energy_ratio = creature.energy / 200
        if energy_ratio < 0.3:
            creature.color = (255, 0, 0)
        elif energy_ratio >= 0.9:
            creature.color = (255, 255, 255)
        elif energy_ratio >= 0.7:
            creature.color = (255, 200, 0)
        else:
            creature.color = (255, 165, 0)

    def _reproduce_creature(self, creature, newborns):
        newborn = creature.reproduce()
        if newborn:
            newborns.append(newborn)
