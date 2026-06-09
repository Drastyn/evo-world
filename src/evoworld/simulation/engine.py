class Engine:
    def __init__(self, world):
        self.world = world

    def tick(self):
        newborns = []
        world_food = self.world.food[:]
        world_creatures = self.world.creatures[:]

        for creature in world_creatures:
            creature.move(self.world.width, self.world.height)
            creature.hungry(creature.energy / 200)

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
