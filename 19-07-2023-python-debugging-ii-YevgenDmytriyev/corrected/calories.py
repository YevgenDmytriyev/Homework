import datetime
# Task 3
# calories.py 
def get_duration_in_minutes(start_time, end_time):
    fmt = "%H:%M"  # Corrected the format
    start = datetime.datetime.strptime(start_time, fmt)
    end = datetime.datetime.strptime(end_time, fmt)
    duration = end - start
    duration_minutes = duration.total_seconds() / 60  # Corrected the calculation for minutes
    return int(duration_minutes)

def calculate_calories_burned(activity):
    calorie_chart = {
        "Running": 600,
        "Cycling": 500,
        "Swimming": 700,
        "Yoga": 300,
        "Push-ups": 300,
        "Sit-ups": 500,
        "Squats": 300,
        "Jumping Jacks": 700,
    }
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")
    duration = get_duration_in_minutes(start_time, end_time)
    calories_per_minute = calorie_chart[activity] / 60  # Calories for each minute
    total_calories = calories_per_minute * duration
    return int(total_calories)
# Testing the functions (to be commented out in the final version)
print(calculate_calories_burned("Running"))