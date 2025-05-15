import json
import random

# Load the exercise dictionary
with open("exercise_dictionary.json", "r") as file:
    exercise_dict = json.load(file)

# Prepare data
group_names = list(exercise_dict.keys())
nof_elements = [len(exercise_dict[group]) for group in group_names]

# Generate random selection
random_indices = [random.randint(1, n) for n in nof_elements]

# Convert indices to exercises
selected_exercises = [
    exercise_dict[group][str(index)]
    for group, index in zip(group_names, random_indices)
]

# Output results
print("Random Indices:", random_indices)
print("Selected Exercises:")
for group, index, exercise in zip(group_names, random_indices, selected_exercises):
    print(f"{group} -> {index}. {exercise}")

