"""
cli.py

Command-line interface for running 2D Solar System simulations.
"""

import argparse
from .run_simulation import run_simulation


def main():
    """
    Parse command-line arguments and run the Solar System simulation.
    """
    parser = argparse.ArgumentParser(
        description="Run a 2D Solar System N-body simulation with visualization."
    )

    parser.add_argument("--nplanets", type=int, default=4,
                        help="Number of planets (including the Sun).")
    parser.add_argument("--steps", type=int, default=10000,
                        help="Number of integration steps.")
    parser.add_argument("--dt", type=float, default=80000,
                        help="Time step [s].")
    parser.add_argument("--method", type=str, choices=["rk4", "euler"], default="rk4",
                        help="Integration method.")
    parser.add_argument("--outfile", type=str, default="orbits.png",
                        help="Output filename for orbit plot.")
    parser.add_argument("--timeseries", type=str, default="timeseries.png",
                        help="Output filename for time series plot.")
    parser.add_argument("--show", action="store_true",
                        help="Display plots interactively.")
    parser.add_argument("--cog", "--CoG", dest="include_cog", action="store_true",
                        help="Compute and plot center of gravity (CoG).")

    args = parser.parse_args()

    run_simulation(
        nplanets=args.nplanets,
        steps=args.steps,
        dt=args.dt,
        method=args.method,
        outfile=args.outfile,
        timeseries=args.timeseries,
        show=args.show,
        include_cog=args.include_cog,
    )


if __name__ == "__main__":
    main()
