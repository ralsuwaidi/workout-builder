from typing import List

from dataclasses import dataclass
import utils.exercises as exercise_utils


@dataclass
class Workout:
    name: str
    muscles: List[str]
    exerciseType: int
    priority: int

    @classmethod
    def get(cls, workout_name):
        workouts = exercise_utils.get_workouts()
        workout = None

        for w in workouts:
            if w["name"] == workout_name:
                workout = w
                break

        if workout is None:
            raise ValueError(f"No workout found with name '{workout_name}'")

        return cls(
            name=workout["name"],
            muscles=workout["muscles"],
            exerciseType=workout["workoutType"],
            priority=workout["priority"],
        )
