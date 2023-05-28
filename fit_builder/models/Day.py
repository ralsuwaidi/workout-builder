from dataclasses import dataclass
from typing import List

from .Exercise import Exercise


@dataclass
class Day:
    exercises: List["Exercise"]
    muscles: List[str]
    day_of_plan: int
