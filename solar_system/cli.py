import argparse
from .run_simulation import run_simulation

def main():
    parser = argparse.ArgumentParser(description="2D N-body Solar System Simulation")
    parser.add_argument("--nplanets", type=int, default=2, help="Number of planets")
    parser.add_argument("--steps", type=int, default=365, help="Number of time steps")
    parser.add_argument("--dt", type=float, default=60*60*24, help="Time step in seconds")
    parser.add_argument("--method", type=str, default="rk4", choices=["rk4", "euler"], help="Integrator")
    parser.add_argument("--outfile", type=str, default="orbits.png", help="Orbit plot output file")
    parser.add_argument("--timeseries", type=str, default="timeseries.png", help="Timeseries plot output file")

    args = parser.parse_args()

    run_simulation(
        nplanets=args.nplanets,
        steps=args.steps,
        dt=args.dt,
        method=args.method,
        outfile=args.outfile,
        timeseries=args.timeseries
    )

if __name__ == "__main__":
    main()
