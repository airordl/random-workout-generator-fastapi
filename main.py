from fastapi import FastAPI
import json
import random
from fastapi.middleware.cors import CORSMiddleware
#ok
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #this, or specify your frontend origin
    allow_methods=["*"],
    allow_headers=["*"],
)


#load data once at startup
with open("exercise_dictionary.json", "r") as f:
    exercise_dict = json.load(f)

#list of exercises groups
group_names = list(exercise_dict.keys())

#whenever someone visits /random-workout, it makes a random workout
@app.get("/random-workout")
def get_random_workout():
    workout = {}
    for group in group_names:
        #for each group
        exercises = exercise_dict[group]
        #pick a random exercise
        index = random.randint(1, len(exercises))
        workout[group] = {
            "index": index,
            "exercise": exercises[str(index)]
        }
    return workout

workout = get_random_workout()
print (workout)
