# 2D Solar System Simulation

A small Python modular project to simulate a 2D solar system using Newtonian gravity.

This is a study project for the master 2 course ScientificSoftware at ENS de Lyon. 

**Author:** Leo Boux de Casson
**Project start date:** September 2025

---

## Features

- Modular functions for gravitational force, acceleration, position, and velocity updates.
- N-body simulation in 2D.
- Configurable number of planets (Sun + N planets).
- Choice of numerical integrator: `Euler` or `RK4`.
- Plotting of 2D trajectories (orbits).
- Optional coordinate timeseries for each planet.
- Optional center-of-gravity (CoG) plotting.
- Unit tests using `pytest`.

## Usage

Run the simulation from the command line:

python main.py --nplanets 4 --steps 10000 --dt 80000 --method rk4 --outfile orbits.png --timeseries timeseries.png --show

**Arguments:**

Option | Description | Default
------ | ----------- | -------
`--nplanets` | Number of planets to simulate (including the Sun) | 2
`--steps` | Number of time steps | 365
`--dt` | Time step in seconds | 86400 (1 day)
`--method` | Integration method: `rk4` or `euler` | rk4
`--outfile` | Filename for orbit plot | orbits.png
`--timeseries` | Filename for coordinate timeseries plot | timeseries.png
`--show` | Show plots interactively | False
`--cog` | Include center-of-gravity subplot in timeseries | False


## Project Structure
```
.
├── solar_system
│ ├── cli.py
│ ├── dynamics.py
│ ├── integration.py
│ ├── planets.py
│ ├── plot_utils.py
│ └── run_simulation.py
├── tests
│ ├── conftest.py
│ └── test_all.py
├── LICENSE
├── main.py
├── README.md
├── orbits.png
└── timeseries.png
```

---

## Installation

1. Clone the repository:

git clone <your-repo-url>
cd Solar_System_2D_test

2. (Optional) Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install numpy matplotlib pytest


## Running Tests

Run all unit tests with:

pytest -v

All key functions in `dynamics`, `integration`, and `planets` are tested.

---

## Contact

For questions or feedback, email me at [leo.bouxdecasson@example.com](mailto:leo.bouxdecasson@example.com).

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


## License

This project is licensed under the [GNU License](./LICENSE).
