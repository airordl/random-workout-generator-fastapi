fetch("http://127.0.0.1:8000/random-workout")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("workout-container");
    for (let group in data) {
      const p = document.createElement("p");
      p.innerHTML = `<strong>${group}</strong>: ${data[group].exercise}`;
      container.appendChild(p);
    }
  });

