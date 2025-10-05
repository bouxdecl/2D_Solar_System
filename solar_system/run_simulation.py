"""
run_simulation.py

Main simulation and plotting logic for the 2D N-body Solar System.
"""

import numpy as np
from .dynamics import compute_accelerations
from .integration import euler_step, rk4_step
from .plot_utils import plot_trajectories, plot_timeseries
from .planets import get_planets, G


def run_simulation(
    nplanets=2,
    steps=365,
    dt=60 * 60 * 24,
    method="rk4",
    outfile="orbits.png",
    timeseries="timeseries.png",
    show=False,
    include_cog=False,
):
    """
    Run a 2D Solar System simulation and produce orbit and time-series plots.

    Parameters
    ----------
    nplanets : int, default=2
        Number of planets to simulate (including the Sun).
    steps : int, default=365
        Number of integration time steps.
    dt : float, default=60*60*24
        Time step [s].
    method : {'rk4', 'euler'}, default='rk4'
        Integration method to use.
    outfile : str, default='orbits.png'
        Filename for saving the orbit plot.
    timeseries : str, default='timeseries.png'
        Filename for saving the time series plot.
    show : bool, default=False
        If True, display the plots interactively.
    include_cog : bool, default=False
        If True, compute and plot the center of gravity (CoG).

    Notes
    -----
    The CoG (center of gravity) is defined as:

    .. math::
        \\mathbf{r}_{\\mathrm{CoG}}(t) = \\frac{\\sum_i m_i \\mathbf{r}_i(t)}{\\sum_i m_i}
    """
    # --- 1. Initialize system ---
    names, masses, positions, velocities = get_planets(nplanets)

    # --- 2. Prepare storage ---
    trajectories = [np.zeros((steps + 1, 2)) for _ in range(nplanets)]
    for i in range(nplanets):
        trajectories[i][0] = positions[i]

    cog_positions = None
    if include_cog:
        cog_positions = np.zeros((steps + 1, 2))
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

        if include_cog:
            cog_positions[step] = np.sum(masses[:, None] * positions, axis=0) / np.sum(masses)

    # --- 5. Plot results ---
    labels = names
    time = np.arange(steps + 1) * dt

    plot_trajectories(trajectories, labels=labels, savefile=outfile, show=show)
    plot_timeseries(time, trajectories, labels=labels,
                    cog_positions=cog_positions if include_cog else None,
                    savefile=timeseries, show=show)

    print(f"✅ Simulation complete — orbit plot saved to '{outfile}', time series saved to '{timeseries}'.")
    if include_cog:
        print("ℹ️ Center of gravity (CoG) included in time-series plot.")
