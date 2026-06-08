import pygame


class Renderer:

    def __init__(self, world, config):
        self.world = world
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode(
            (
                world.width * config.CELL_SIZE,
                world.height * config.CELL_SIZE,
            )
        )

    def draw(self):
        self.screen.fill((0, 0, 0))
        for food in self.world.food:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                (
                    food.x * self.config.CELL_SIZE,
                    food.y * self.config.CELL_SIZE,
                    self.config.CELL_SIZE,
                    self.config.CELL_SIZE,
                ),
            )

        for creature in self.world.creatures:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (
                    creature.x * self.config.CELL_SIZE,
                    creature.y * self.config.CELL_SIZE,
                    self.config.CELL_SIZE,
                    self.config.CELL_SIZE,
                ),
            )

        pygame.display.flip()
