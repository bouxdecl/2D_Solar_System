"""
plot_utils.py

Visualization utilities for 2D N-body Solar System simulations.
Provides trajectory and time-series plotting functions.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_trajectories(trajectories, labels=None, savefile=None, show=True):
    """
    Plot 2D trajectories of all bodies in the simulation.

    Parameters
    ----------
    trajectories : list of ndarray
        List of arrays, each of shape (steps, 2), giving the (x, y) coordinates of each body.
    labels : list of str, optional
        Names or identifiers for each trajectory.
    savefile : str, optional
        File path to save the figure.
    show : bool, default=True
        Whether to display the figure interactively.

    Notes
    -----
    This function displays the orbits in the xy-plane, with equal aspect ratio:

    .. math::
        r_i(t) = (x_i(t), y_i(t))
    """
    plt.figure(figsize=(6, 6))
    for i, traj in enumerate(trajectories):
        x, y = traj[:, 0], traj[:, 1]
        if labels:
            plt.plot(x, y, label=labels[i])
        else:
            plt.plot(x, y)

    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.axis("equal")
    if labels:
        plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)

    if savefile:
        plt.savefig(savefile, dpi=150)
    if show:
        plt.show()
    else:
        plt.close()

def plot_timeseries(time, trajectories, labels=None, cog_positions=None,
                    savefile=None, show=True):
    """
    Plot x(t) and y(t) coordinates for each body, with optional CoG subplot.

    Parameters
    ----------
    time : ndarray, shape (steps,)
        Time array [s].
    trajectories : list of ndarray
        List of arrays, each of shape (steps, 2), giving the (x, y) coordinates of each body.
    labels : list of str, optional
        Names or identifiers for each body.
    cog_positions : ndarray, shape (steps, 2), optional
        Center-of-gravity trajectory [m]. If provided, adds one extra subplot at the bottom.
    savefile : str, optional
        File path to save the figure.
    show : bool, default=True
        Whether to display the figure interactively.

    Notes
    -----
    Each subplot shows:

    .. math::
        x_i(t), \\; y_i(t)

    If `cog_positions` is given, an additional subplot is added showing:

    .. math::
        r_{\\mathrm{CoG}}(t) = \\frac{\\sum_i m_i r_i(t)}{\\sum_i m_i}
    """
    n = len(trajectories)
    n_subplots = n + 1 if cog_positions is not None else n
    fig, axes = plt.subplots(n_subplots, 1, figsize=(8, 2 * n_subplots), sharex=True)

    if n_subplots == 1:
        axes = [axes]

    # --- Plot planets ---
    for i, traj in enumerate(trajectories):
        x, y = traj[:, 0], traj[:, 1]
        axes[i].plot(time, x, label="x")
        axes[i].plot(time, y, label="y")
        axes[i].set_ylabel("Position [m]")
        axes[i].legend()
        if labels:
            axes[i].set_title(labels[i])
        axes[i].grid(True, linestyle="--", alpha=0.5)

    # --- Plot CoG if available ---
    if cog_positions is not None:
        ax_cog = axes[-1]
        ax_cog.plot(time, cog_positions[:, 0], "--", color="k", label="CoG x")
        ax_cog.plot(time, cog_positions[:, 1], "--", color="r", label="CoG y")
        ax_cog.set_ylabel("Position [m]")
        ax_cog.set_title("Center of Gravity")
        ax_cog.legend()
        ax_cog.grid(True, linestyle="--", alpha=0.5)

    axes[-1].set_xlabel("Time [s]")
    fig.tight_layout()

    if savefile:
        plt.savefig(savefile, dpi=150)
    if show:
        plt.show()
    else:
        plt.close()
