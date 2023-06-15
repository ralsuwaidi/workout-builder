from dataclasses import dataclass
from typing import List

from .Workout import Workout
from .Muscle import Muscle


@dataclass
class Day:
    """
    Generates a day of exercise based on
    1. The priority
    2. if the exercise is compound or not
    """

    muscles: List[str]
    workouts: List["Workout"] = None
    day_of_plan: int = None
    workout_variery = 'med'

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

    def remove_excess(self):
        # remove most of the excess workouts besides the lowest

        # if 2 muscles we have 20 sets spread out between each
        # veriery can be low, med or high where
        # high mixes a lot of exercises and low 
        # tries to keep the number of exercises low but the 
        # set number for each high

        # low vaiety choose every muscle once to get 20 total
        if self.workout_variery == 'low':
            viewed_muscle = set()
            trimmed_workout_list = []

            for workout in self.workouts:
                current_muscle = workout.muscles[0]
                if current_muscle not in viewed_muscle:
                    trimmed_workout_list.append(workout)
                    viewed_muscle.add(current_muscle)

            self.workouts = trimmed_workout_list
        


    def order_workouts(self):
        # keep compound first
        self.workouts.sort(key=lambda w: w.points, reverse=True)

        for w in self.workouts:
            print(f'{w.name}: {w.points}')

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
