## Project Scope

Command line application that gives a workout plan based on user input and requirement. The plan should follow best 'rules' that are derived from fitness research and literature. The project should have the following

1. A way for users to choose their program
2. A way to customize the program
3. A way to see what rules the program follows and what rules it doesnt
4. A way to see the plan for the day
5. A way to update the plan based on previous days workout result

## Data Structure

### Plan

days: list of days
exercise_per_week: the number of exercises per week (user controlled)
muscle_focus: list of muscle focus (based on user preference)
weeks: number of weeks this plan follows

### Day

exercises: List of exercises
muslces: list of targeted muscles, based on priority
day_of_plan: a number based on the day of the plan

### Exercise

name: Name of the chosen workout
reps: number of reps
sets: number of sets
volume: volume (sets x reps)
target_reps: targeted reps
target_sets: targeted sets
target_volume: targeted volume
muscles: list of muscles the exercise targets
intensity: how intense the exercise should be using an RPE model (more info below)
failed: boolean, if the exercise was completed or not

### Muscle

name: name of muscle
workouts: list of workouts

### Workout

name: name of the workout (eg: overhead barbell press)
muscles: list of muscles it targets
exerciseType: 1/2 (for isolated or compound respectively)
priority: how important the exercise is (if it has a higher correlation to hypertrophy than it gets a higher number 1-5)

### Notes

- RPE: Rate of perceived exertion (RPE): This method involves subjectively rating how hard an exercise feels on a scale of 1-10. A rating of 1 would indicate very light exercise, while a rating of 10 would indicate maximal effort

## Example Exercises

### Example Day

- Flat Barbell Bench Press: 3x5 [chest]
- Seated (or Standing) Barbell Shoulder/Overhead Press: 3x5 [shoulder]
- Incline Barbell Bench Press: 3x5 [chest]
- Dumbbell Side Lateral Raise: 3x10-12 [shoulder]
- Rope Pushdowns (circuit machine): 3x10-12 [triceps]
- Overhead Dumbbell Extension or similar triceps exercise: 3x10-12 [triceps]
- Shrugs(circuit machine or dumbbells): 3x10-12 [traps]

## TODO

