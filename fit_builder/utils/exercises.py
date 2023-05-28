import os

import yaml


def verify_muscles(workouts, muscles):
    for workout in workouts:
        for muscle in workout["muscles"]:
            if muscle not in muscles:
                raise ValueError(
                    f"Invalid muscle '{muscle}' in workout '{workout['name']}'"
                )


def verify_priority(workouts):
    for workout in workouts:
        if workout["priority"] < 1 or workout["priority"] > 5:
            raise ValueError(
                f"Invalid priority '{workout['priority']}' in workout '{workout['name']}'"
            )


def verify_workouts(workouts_file_path):
    with open(workouts_file_path, "r") as stream:
        data = yaml.safe_load(stream)
        workouts = data["workouts"]
        muscles = data["muscles"]

    verify_muscles(workouts, muscles)
    verify_priority(workouts)

    print("Workouts file verified successfully")


def get_workouts():
    """returns a list of workouts from yaml file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yml_path = os.path.join(current_dir, "..", "workouts.yml")
    with open(yml_path, "r") as stream:
        data = yaml.safe_load(stream)
        workouts = data["workouts"]

    return workouts
