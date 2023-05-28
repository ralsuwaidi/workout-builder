from typing import List

from .Day import Day


from dataclasses import dataclass


@dataclass
class Plan:
    days: List["Day"]
    exercise_per_week: int
    muscle_focus: List[str]
    weeks: int
