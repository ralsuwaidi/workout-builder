from dataclasses import dataclass
from typing import List

from .Workout import Workout
from .Exercise import Exercise
from .Muscle import Muscle


@dataclass
class Day:
    """
    Generates a day of exercise based on
    1. The priority
    2. if the exercise is compound or not
    """

    muscles: List[str]
    exercises: List["Exercise"] = None
    workouts: List["Workout"] = None
    day_of_plan: int = None

    @classmethod
    def muscles_to_day(cls, muscle_list: List["str"]) -> "Day":
        workouts_list = []
        for muscle in muscle_list:
            workouts = Muscle.workouts_by_muscle(muscle)
            workouts_list.extend(workouts)

        if len(workouts_list) == 0:
            raise ValueError(f"No workouts found for muscle '{muscle_list}'")

        return Day(muscles=muscle_list, workouts=workouts_list)

    @classmethod
    def convert_to_day(cls, workout_list: List["Workout"]) -> "Day":
        """
        This function orders and removes exess workouts
        """
        pass

    def order_workouts(self):
        # Orders workouts based on priority
        self.workouts.sort(key=lambda w: w.priority, reverse=True)

    def generate_day(self):
        """
        generates a day of exercise based on predefined variables

        given
        1. muscles: List[str]
        2.
        """
        pass

    def __repr__(self) -> str:
        # TODO: Improve this
        return f"Day({[w.name for w in self.workouts]})"
