from typing import List
from utils.exercises import get_workouts

from .Workout import Workout


class Muscle:
    def __init__(self, name):
        self.name = name
        self.workouts = Muscle.workouts_by_muscle(name)

    @classmethod
    def workouts_by_muscle(cls, muscle) -> List["Workout"]:
        workouts = get_workouts()
        muscle_workouts = [w for w in workouts if muscle in w["muscles"]]
        workout_list = []

        for workout in muscle_workouts:
            workout_obj = Workout(
                name=workout["name"],
                muscles=workout["muscles"],
                workoutType=workout["workoutType"],
                priority=workout["priority"],
            )
            workout_list.append(workout_obj)

        if len(workout_list) == 0:
            raise ValueError(f"No workouts found for muscle '{muscle}'")
        return workout_list
