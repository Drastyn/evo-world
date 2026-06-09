import pygame

from src.evoworld.domain.world import World
from src.evoworld.rendering.renderer import Renderer
from src.evoworld.simulation.engine import Engine

world = World()
world.spawn_food()
world.spawn_creatures()

renderer = Renderer(world)
engine = Engine(world)

clock = pygame.time.Clock()

while running := True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    engine.tick()
    renderer.draw()
    clock.tick(10)
