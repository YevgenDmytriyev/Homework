Task 1 - Recursive User Authentication

In the auth.py module, a recursive function authenticate_user() has been implemented to efficiently handle user authentication. If the provided credentials are incorrect, the function prompts the user to enter valid credentials until they are authenticated.

Task 2 - Customizable Workout Plan

In the workout.py module, the generate_workout_plan() function allows the user to create a customizable workout plan. The user can specify the number of activities they want in their plan, and the function ensures that the plan includes unique activities based on random selection.

Task 3 - Calorie Calculation and Duration

The calories.py module contains functions for calculating calories burned during different activities. The calculate_calories_burned(activity) function computes calories burned based on the duration of the activity. Additionally, the get_duration_in_minutes(start_time, end_time) function calculates the duration in minutes between two time points.

Task 4 - Progress Tracking

The progress.py module includes the update_progress(progress, workout) function. This function allows for easy tracking of workout progress. It updates the progress dictionary with the number of times each workout has been completed. The provided testing code demonstrates its functionality.

Task 5 - Logging Activities

Within the log.py module, the log_activity(activity) function is designed to log various activities. It appends each activity to an external file called activity_log.txt. The function opens the file in "append" mode to avoid overwriting existing data.

Task 6 - Main Program Execution

The main.py script serves as the entry point for the user's interaction. It orchestrates the entire process, from user authentication to workout planning, progress tracking, and calorie calculation. If the user's authentication fails, the script utilizes recursion to provide another chance for correct authentication.

