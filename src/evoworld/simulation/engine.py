from src.evoworld.config.settings import CREATURE_REPRODUCTION_ENERGY


class Engine:
    def __init__(self, world):
        self.world = world

    def tick(self):
        newborns = []
        world_food = self.world.food[:]
        world_creatures = self.world.creatures[:]

        for creature in world_creatures:
            food = creature.find_nearest_food(self.world.food)
            if food:
                creature.move_towards(food)
            else:
                creature.move_random(self.world.width, self.world.height)
            creature.hungry(creature.energy / CREATURE_REPRODUCTION_ENERGY)
            for food in world_food:
                if creature.eat(food):
                    self.world.food.remove(food)
                    break
            if creature.death():
                self.world.creatures.remove(creature)
                continue
            newborn = creature.reproduce()
            if newborn:
                newborns.append(newborn)
        self.world.creatures.extend(newborns)
        self.world.spawn_food(
            max(1, len(self.world.creatures) // 5),
        )
