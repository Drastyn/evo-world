from dataclasses import dataclass
import random


@dataclass
class Creature:
    x: int
    y: int
    energy: int

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
