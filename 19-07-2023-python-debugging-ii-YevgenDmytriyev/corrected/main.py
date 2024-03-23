import auth, calories, log, progress, workout
import sys
from auth import authenticate_user
from workout import generate_workout_plan
from progress import update_progress
from calories import calculate_calories_burned
from log import log_activity
# Import the necessary functions from your custom modules

# Task 6
# main.py 
def main():
    user_progress = {
        "Running": 0, "Cycling": 0, "Swimming": 0, "Yoga": 0,
        "Push-ups": 0, "Sit-ups": 0, "Squats": 0, "Jumping Jacks": 0
    }
    
    burned_calories = {
        "Running": 0, "Cycling": 0, "Swimming": 0, "Yoga": 0,
        "Push-ups": 0, "Sit-ups": 0, "Squats": 0, "Jumping Jacks": 0
    }

    if authenticate_user():
        workout_plan = generate_workout_plan()
        print(f"Your workout plan for today: {workout_plan}")

        for activity in workout_plan:
            user_progress = update_progress(user_progress, activity)
            log_activity(activity)

            burned = calculate_calories_burned(activity)
            burned_calories[activity] += burned
            print(f"You burned {burned} calories doing {activity}!")

        print("\nYour progress for today:")
        for activity, count in user_progress.items():
            print(f"{activity}: {count} times")

        print("\nTotal calories burned today:")
        for activity, calories in burned_calories.items():
            print(f"{activity}: {calories} calories")
    else:
        print("User is invalid. Please try again.")
        main()

if __name__ == "__main__":
    main()