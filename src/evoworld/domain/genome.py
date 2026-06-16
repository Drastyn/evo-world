from dataclasses import dataclass
import random


@dataclass
class Genome:
    vision: int

    def mutate(self) -> "Genome":
        return Genome(vision=max(1, self.vision + random.choice([-1, 0, 1])))
