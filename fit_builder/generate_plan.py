import yaml

import models


def generate_plan(days_per_week):
    """
    generates workout plan based on the user input

    1. days per week: int
    2. muscle focus: eg 'chest', 'back'
    """

    day = models.Day.muscles_to_day(["chest", "shoulder", "triceps"])
    print(day)
    day.order_workouts()
    day.remove_excess('low')
    return day


if __name__ == "__main__":
    print(generate_plan(2))
