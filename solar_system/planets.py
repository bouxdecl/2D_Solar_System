"""
Planetary data for a simple 2D solar system model.
All values are approximate, assuming circular orbits.
Units: mass [kg], distance [m], velocity [m/s].
"""

import numpy as np

# Universal gravitational constant [m^3 kg^-1 s^-2]
G = 6.67430e-11

# Planetary data
PLANETS = [
    {"name": "Sun",     "mass": 1.989e30, "r": 0.0,      "v": 0.0},
    {"name": "Mercury", "mass": 3.285e23, "r": 5.79e10,  "v": 47400},
    {"name": "Venus",   "mass": 4.867e24, "r": 1.082e11, "v": 35000},
    {"name": "Earth",   "mass": 5.972e24, "r": 1.496e11, "v": 29780},
    {"name": "Mars",    "mass": 6.39e23,  "r": 2.279e11, "v": 24100},
    {"name": "Jupiter", "mass": 1.898e27, "r": 7.785e11, "v": 13070},
    {"name": "Saturn",  "mass": 5.683e26, "r": 1.433e12, "v": 9680},
    {"name": "Uranus",  "mass": 8.681e25, "r": 2.877e12, "v": 6800},
    {"name": "Neptune", "mass": 1.024e26, "r": 4.503e12, "v": 5430},
]


def get_planets(nplanets):
    """
    Return initial conditions for the first `nplanets` in PLANETS.

    Parameters
    ----------
    nplanets : int
        Number of planets to include (including the Sun).

    Returns
    -------
    names : list[str]
        Names of selected planets.
    masses : ndarray
        Masses of planets [kg].
    positions : ndarray
        Initial 2D positions [m].
    velocities : ndarray
        Initial 2D velocities [m/s].
    """
    nplanets = min(nplanets, len(PLANETS))
    subset = PLANETS[:nplanets]

    names = [p["name"] for p in subset]
    masses = np.array([p["mass"] for p in subset])
    positions = np.zeros((nplanets, 2))
    velocities = np.zeros((nplanets, 2))

    for i, p in enumerate(subset):
        # Place planets on x-axis, with counterclockwise circular velocity
        positions[i] = np.array([p["r"], 0.0])
        velocities[i] = np.array([0.0, p["v"]])

    return names, masses, positions, velocities
