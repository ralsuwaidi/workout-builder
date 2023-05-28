from dataclasses import dataclass
from typing import List

from .Workout import Workout


@dataclass
class Muscle:
    name: str
    workouts: List["Workout"]
