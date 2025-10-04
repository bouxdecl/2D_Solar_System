import matplotlib.pyplot as plt
import numpy as np

def plot_trajectories(trajectories, labels=None, savefile=None, show=True):
    """
    Plot 2D trajectories of bodies.
    """
    plt.figure(figsize=(6,6))
    for i, traj in enumerate(trajectories):
        x, y = traj[:,0], traj[:,1]
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

def plot_timeseries(time, trajectories, labels=None, cog_positions=None, savefile=None, show=True):
    """
    Plot subplots of x and y coordinates vs time for each body,
    and optionally plot the center of gravity.
    """
    n = len(trajectories)
    fig, axes = plt.subplots(n, 1, figsize=(8, 2*n), sharex=True)
    if n == 1:
        axes = [axes]

    for i, traj in enumerate(trajectories):
        x = traj[:,0]
        y = traj[:,1]
        axes[i].plot(time, x, label="x")
        axes[i].plot(time, y, label="y")
        axes[i].set_ylabel("Position [m]")
        axes[i].legend()
        if labels:
            axes[i].set_title(labels[i])
        axes[i].grid(True, linestyle="--", alpha=0.5)

    # Plot CoG on the last subplot
    if cog_positions is not None:
        axes[-1].plot(time, cog_positions[:,0], '--', color='k', label='CoG x')
        axes[-1].plot(time, cog_positions[:,1], '--', color='r', label='CoG y')
        axes[-1].legend()

    axes[-1].set_xlabel("Time [s]")
    fig.tight_layout()

    if savefile:
        plt.savefig(savefile, dpi=150)

    if show:
        plt.show()
    else:
        plt.close()
