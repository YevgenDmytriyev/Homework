# Task 4
# progress.py 
def update_progress(progress, workout):
    if workout not in progress:  # Handle the scenario where the workout isn't already in the progress dict
        progress[workout] = 0
    progress[workout] += 1
    return progress  # It's a good practice to return the updated data
# Testing the function (to be commented out in the final version)
test_progress = {
    "Running": 0,
    "Cycling": 0,
}
updated_progress = update_progress(test_progress, "Running")
updated_progress