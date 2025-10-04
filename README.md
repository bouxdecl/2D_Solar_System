
# 2D Solar System Simulation

A small Python modular project to simulate a 2D solar system using Newtonian gravity.

author : Leo Boux de Casson 

project start date : septembre 2025


## Features

- Modular functions for gravitational force, acceleration, position, and velocity updates.
- N-body simulation in 2D.
- Configurable number of planets (Sun + N-planets).
- choice of integrator method
- Plotting of 2D trajectories (orbits).
- Optional coordinate timeseries.
- Unit tests using `pytest`.

## Usage
```bash
python main.py  --nplanets 4 --steps 10000 --dt 80000 
```

---

## Structure

```.
├── solar_system
│   ├── cli.py
│   ├── dynamics.py
│   ├── planets.py
│   ├── plot_utils.py
│   ├── __pycache__
│   └── run_simulation.py
├── tests
│   ├── conftest.py
│   ├── initial_y,
│   ├── __pycache__
│   └── test_all.py
├── LICENSE
├── main.py
├── orbits.png
├── README.md
└── timeseries.png
```



## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Solar_System_2D_test
```


## Contact

For questions or feedback, email me at [leo.bouxdecasson@example.com](mailto:leo.bouxdecasson@example.com)

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Licence
Here's the [GNU licence](./LICENCE)