"""
integration.py

Contains numerical integration schemes for updating positions and velocities.
"""

import numpy as np
from .dynamics import compute_accelerations


def euler_step(positions, velocities, masses, dt, G):
    """
    Advance one time step using the explicit Euler method.
    """
    acc = compute_accelerations(positions, masses, G)
    new_velocities = velocities + acc * dt
    new_positions = positions + new_velocities * dt
    return new_positions, new_velocities


def rk4_step(positions, velocities, masses, dt, G):
    """
    Advance one time step using the 4th-order Runge–Kutta (RK4) integrator.
    """
    # k1
    a1 = compute_accelerations(positions, masses, G)
    k1v = a1 * dt
    k1x = velocities * dt

    # k2
    a2 = compute_accelerations(positions + 0.5 * k1x, masses, G)
    k2v = a2 * dt
    k2x = (velocities + 0.5 * k1v) * dt

    # k3
    a3 = compute_accelerations(positions + 0.5 * k2x, masses, G)
    k3v = a3 * dt
    k3x = (velocities + 0.5 * k2v) * dt

    # k4
    a4 = compute_accelerations(positions + k3x, masses, G)
    k4v = a4 * dt
    k4x = (velocities + k3v) * dt

    # Combine increments
    new_positions = positions + (k1x + 2*k2x + 2*k3x + k4x) / 6
    new_velocities = velocities + (k1v + 2*k2v + 2*k3v + k4v) / 6

    return new_positions, new_velocities
