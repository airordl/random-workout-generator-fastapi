#  Random Workout Generator

This project generates a random workout using FastAPI (Python) for the backend and HTML+JavaScript for the frontend.
It selects one random exercise from each muscle group, compound movement or full body, every time the user loads the page.


---
##  Pros & Cons of Randomized Training (Strength vs. Hypertrophy)

This app generates randomized workout plans. While variety can be fun and useful, it's important to understand the implications for different training goals — especially **strength** and **hypertrophy**.

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

