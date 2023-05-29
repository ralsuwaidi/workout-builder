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

    @classmethod
    def get_by_muscle(cls, muscle) -> List["Workout"]:
        workouts = exercise_utils.get_workouts()
        muscle_workouts = [w for w in workouts if muscle in w["muscles"]]
        muscle_workouts_obj = []

        for workout in muscle_workouts:
            workout_obj = cls(
                name=workout["name"],
                muscles=workout["muscles"],
                exerciseType=workout["workoutType"],
                priority=workout["priority"],
            )
            muscle_workouts_obj.append(workout_obj)

        if len(muscle_workouts_obj) == 0:
            raise ValueError(f"No workouts found for muscle '{muscle}'")
        return muscle_workouts_obj
