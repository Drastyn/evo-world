import pygame

import evoworld.config.settings as settings
from src.evoworld.domain.world import World
from src.evoworld.rendering.renderer import Renderer
from src.evoworld.simulation.engine import Engine

world = World(width=settings.WORLD_WIDTH, height=settings.WORLD_HEIGHT)
world.spawn_food(settings.INITIAL_FOOD, settings.MAX_FOOD)
world.spawn_creatures(settings.INITIAL_CREATURES, settings.INITIAL_ENERGY)

renderer = Renderer(world, settings)
engine = Engine(world, settings)

clock = pygame.time.Clock()

while running := True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    engine.tick()
    renderer.draw()
    clock.tick(10)
