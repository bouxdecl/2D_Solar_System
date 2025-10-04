"""
run_simulation.py

Main simulation and plotting logic for 2D N-body Solar System.
"""

import numpy as np
from .dynamics import compute_accelerations
from .integration import euler_step, rk4_step
from .plot_utils import plot_trajectories, plot_timeseries
from .planets import get_planets, G

G = 6.67430e-11  # gravitational constant


def run_simulation(nplanets=2, steps=365, dt=60*60*24, method="rk4",
                   outfile="orbits.png", timeseries="timeseries.png"):
    """
    Run a 2D Solar System simulation and produce plots.

    Args:
        nplanets (int): number of planets
        steps (int): number of integration steps
        dt (float): timestep in seconds
        method (str): integration method ('rk4' or 'euler')
        outfile (str): output filename for orbit plot
        timeseries (str): output filename for time series plot
    """
    # --- 1. Initialize system ---
    names, masses, positions, velocities = get_planets(nplanets)

    # --- 2. Prepare storage ---
    trajectories = [np.zeros((steps + 1, 2)) for _ in range(nplanets)]
    cog_positions = np.zeros((steps + 1, 2))
    for i in range(nplanets):
        trajectories[i][0] = positions[i]
    cog_positions[0] = np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)

    # --- 3. Select integrator ---
    if method == "euler":
        step_func = euler_step
    elif method == "rk4":
        step_func = rk4_step
    else:
        raise ValueError("Unknown method. Choose 'rk4' or 'euler'.")

    # --- 4. Main time loop ---
    for step in range(1, steps + 1):
        positions, velocities = step_func(positions, velocities, masses, dt, G)

        for i in range(nplanets):
            trajectories[i][step] = positions[i]

        cog_positions[step] = np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)

    # --- 5. Plot results ---
    labels = ["Sun"] + [f"Planet {i}" for i in range(1, nplanets)]
    time = np.arange(steps + 1) * dt

    plot_trajectories(trajectories, labels=labels, savefile=outfile, show=False)
    plot_timeseries(time, trajectories, labels=labels, cog_positions=cog_positions,
                    savefile=timeseries, show=False)

    print(f"Simulation complete — orbit plot saved to {outfile}, timeseries saved to {timeseries}")
