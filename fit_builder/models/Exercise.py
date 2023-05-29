from dataclasses import dataclass
from typing import List

from .Workout import Workout


@dataclass
class Exercise:
    name: str
    reps: int
    sets: int
    muscles: List[str]
    target_reps: int = None
    intensity: int = 5
    target_sets: int = None
    failed: bool = False

    def __post_init__(self):
        if not 1 <= self.intensity <= 10:
            raise ValueError("Intensity must be between 1 and 10.")

    @property
    def volume(self):
        return self.reps * self.sets

    @property
    def target_volume(self):
        return self.target_reps * self.target_sets

    @classmethod
    def create_exercise(cls, exercise_name, reps, sets):
        workout = Workout.get(exercise_name)
        return cls(name=workout.name, reps=reps, sets=sets, muscles=workout.muscles)
