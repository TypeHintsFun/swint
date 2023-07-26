from __future__ import annotations

from dataclasses import dataclass
import math

from base.field import Field
from consts import AURA_RADIUS


@dataclass
class Ant:
    x: int
    y: int

    field: Field

    def iter_near_ants(self, max_radius: int = AURA_RADIUS):
        for ant in self.field.ants:
            if (self.get_distance_for(ant) <= max_radius) and (ant is not self):
                yield ant

    def get_distance_for(self, other_ant: Ant) -> float:
        return math.sqrt(((self.x - other_ant.x) ** 2) + ((self.y - other_ant.y) ** 2))
