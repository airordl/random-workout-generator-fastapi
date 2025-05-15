#  Random Workout Generator

This project generates a random workout using FastAPI (Python) for the backend and HTML+JavaScript for the frontend.
It selects one random exercise from each muscle group, compound movement or full body, every time the user loads the page.


---
##  Pros & Cons of Randomized Training (Strength vs. Hypertrophy)

This app generates randomized workout plans. While variety can be fun and useful, it's important to understand the implications for different training goals — especially **strength** and **hypertrophy**.

---

###  Strength Training

|  Pros |  Cons |
|--------|---------|
| Reduces overuse injuries from repeated heavy movements | Lack of consistency can hinder progressive overload |
| Encourages movement variety and skill development | No guarantee of hitting all major lifts regularly |
| Keeps training mentally fresh | Difficult to track progress on compound lifts |

---

###  Hypertrophy Training (Muscle Growth)

|  Pros | Cons |
|--------|---------|
| Hits muscles from different angles for balanced development | May not provide enough volume per muscle group per session |
| Fun and engaging, prevents boredom | Hard to apply progressive overload systematically |
| Useful for general fitness or variety days | Random selection can neglect key hypertrophy principles like time under tension or intensity |

---

### When Randomized Training Works Best

-  Beginners building general movement experience
-  Cross-training, functional fitness, or “fun” sessions
-  Maintenance workouts or travel/limited-equipment routines
-  Mental variety to stay engaged

---

###  When It’s Not Ideal

-  Serious strength athletes (powerlifting, Olympic lifting)
-  Bodybuilders or physique-focused programs
-  Anyone following a strict progressive training plan

---

**Conclusion:**

Randomized training is great for **novelty**, **general fitness**, or **casual users**, but should be used carefully or supplemented with structured progression for serious strength or hypertrophy goals.

---

## Requirements

- Python 3.8+
- `fastapi`
- `uvicorn`

Install dependencies with:

```bash
pip install fastapi uvicorn
```

---

## Project Structure

All files are in one folder:

```
project/
├── main.py                     ← FastAPI backend (root)
├── exercise_dictionary.json    ← Exercise data (root)
├── frontend/                   ← Frontend folder
│   ├── index.html              ← HTML UI
│   └── script.js               ← JavaScript logic
├── README.md                   ← Documentation
├── .gitignore                  ← Git ignore rules

```

---

Run main.py it with:

```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/random-workout](http://127.0.0.1:8000/random-workout) or [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test.

---

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open `index.html` in your browser.

3. See your random workout appear on the page and refresh the page for a new set of random workouts

---

##  Notes

- The backend uses a JSON dictionary to simulate a database.
- The frontend fetches data from the FastAPI endpoint.
- CORS is enabled so the browser can connect locally.
- You can easily deploy the backend with Render or Railway and host the frontend on Netlify or GitHub Pages.

---

##  Author

Created by airordl  
GitHub: [https://github.com/airordl](https://github.com/airordl)

