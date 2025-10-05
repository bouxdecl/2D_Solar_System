"""
integration.py

Numerical integration schemes for updating positions and velocities
in the 2D N-body Solar System simulation.
"""

import numpy as np
from .dynamics import compute_accelerations


def euler_step(positions, velocities, masses, dt, G):
    """
    Advance one time step using the explicit Euler method.

    Parameters
    ----------
    positions : ndarray, shape (N, 2)
        Current positions [m].
    velocities : ndarray, shape (N, 2)
        Current velocities [m/s].
    masses : ndarray, shape (N,)
        Masses [kg].
    dt : float
        Time step [s].
    G : float
        Gravitational constant [m³ kg⁻¹ s⁻²].

    Returns
    -------
    new_positions : ndarray, shape (N, 2)
        Updated positions [m].
    new_velocities : ndarray, shape (N, 2)
        Updated velocities [m/s].

    Notes
    -----
    Euler scheme (1st order):

    .. math::
        v_{n+1} = v_n + a_n \, \Delta t \\
        x_{n+1} = x_n + v_{n+1} \, \Delta t
    """
    acc = compute_accelerations(positions, masses, G)
    new_velocities = velocities + acc * dt
    new_positions = positions + new_velocities * dt
    return new_positions, new_velocities


def rk4_step(positions, velocities, masses, dt, G):
    """
    Advance one time step using the 4th-order Runge–Kutta (RK4) integrator.

    Parameters
    ----------
    positions : ndarray, shape (N, 2)
        Current positions [m].
    velocities : ndarray, shape (N, 2)
        Current velocities [m/s].
    masses : ndarray, shape (N,)
        Masses [kg].
    dt : float
        Time step [s].
    G : float
        Gravitational constant [m³ kg⁻¹ s⁻²].

    Returns
    -------
    new_positions : ndarray, shape (N, 2)
        Updated positions [m].
    new_velocities : ndarray, shape (N, 2)
        Updated velocities [m/s].

    Notes
    -----
    Classical RK4 scheme (4th order):

    .. math::
        k_1 = f(t_n, y_n) \\
        k_2 = f(t_n + \tfrac{1}{2}\Delta t, y_n + \tfrac{1}{2}\Delta t k_1) \\
        k_3 = f(t_n + \tfrac{1}{2}\Delta t, y_n + \tfrac{1}{2}\Delta t k_2) \\
        k_4 = f(t_n + \Delta t, y_n + \Delta t k_3) \\
        y_{n+1} = y_n + \tfrac{\Delta t}{6}(k_1 + 2k_2 + 2k_3 + k_4)
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

    new_positions = positions + (k1x + 2*k2x + 2*k3x + k4x) / 6
    new_velocities = velocities + (k1v + 2*k2v + 2*k3v + k4v) / 6
    return new_positions, new_velocities
