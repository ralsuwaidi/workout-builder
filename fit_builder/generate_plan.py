import yaml

import models


def generate_plan(days_per_week):
    """
    generates workout plan based on the user input

    1. days per week: int
    2. muscle focus: eg 'chest', 'back'
    """

    return models.Workout.get_by_muscle("shoulder")


if __name__ == "__main__":
    print(generate_plan(2))
