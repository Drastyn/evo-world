import pygame
from src.evoworld.config.settings import RENDERER_CELL_SIZE


class Renderer:

    def __init__(self, world):
        self.world = world
        pygame.init()
        self.screen = pygame.display.set_mode(
            (
                world.width * RENDERER_CELL_SIZE,
                world.height * RENDERER_CELL_SIZE,
            )
        )

    def draw(self):
        self.screen.fill((0, 0, 0))
        for food in self.world.food:
            self._draw_food(food)

        for creature in self.world.creatures:
            self._draw_creature(creature)

        pygame.display.flip()

    def _draw_food(self, food):
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (
                food.x * RENDERER_CELL_SIZE,
                food.y * RENDERER_CELL_SIZE,
                RENDERER_CELL_SIZE,
                RENDERER_CELL_SIZE,
            ),
        )

    def _draw_creature(self, creature):
        pygame.draw.rect(
            self.screen,
            creature.color,
            (
                creature.x * RENDERER_CELL_SIZE,
                creature.y * RENDERER_CELL_SIZE,
                RENDERER_CELL_SIZE,
                RENDERER_CELL_SIZE,
            ),
        )
