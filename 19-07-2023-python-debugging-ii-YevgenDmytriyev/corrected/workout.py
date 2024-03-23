import random
# Task 2
# workout.py 
def generate_workout_plan():
    workouts = [
        "Push-ups",
        "Sit-ups",
        "Squats",
        "Jumping Jacks",
        "Running",
        "Cycling",
        "Swimming",
        "Yoga"
    ]
    num_activities = int(input("How many activities would you like in your workout plan? "))
    # Ensure the user doesn't ask for more activities than available
    num_activities = min(num_activities, len(workouts))
    workout_plan = random.sample(workouts, num_activities)  # Using random.sample to get unique workouts
    return workout_plan
# Testing the function (to be commented out in the final version)
generate_workout_plan()