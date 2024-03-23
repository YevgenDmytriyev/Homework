# Task 5
# log.py 
def log_activity(activity):
    with open("activity_log.txt", "a") as file:  # Change mode to 'a' for appending instead of overwriting
        file.write(activity + "\n")
# Testing the function (to be commented out in the final version)
log_activity("Running")