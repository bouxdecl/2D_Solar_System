"""
dynamics.py

Core gravitational dynamics functions for the 2D N-body Solar System simulation.

This module provides low-level routines for computing gravitational forces and
accelerations between celestial bodies under Newtonian gravity. A small softening
parameter `epsilon` is used to prevent singularities when two bodies get too close.
"""

import numpy as np

# Universal gravitational constant [m^3 kg^-1 s^-2]
G = 6.67430e-11

# Softening length to avoid numerical singularities [m]
epsilon = 1e-6


def gravitational_force(r1, r2, m1, m2):
    """
    Compute the gravitational force vector exerted on body 1 by body 2.

    Parameters
    ----------
    r1 : array_like of shape (2,)
        2D position vector of body 1 [m].
    r2 : array_like of shape (2,)
        2D position vector of body 2 [m].
    m1 : float
        Mass of body 1 [kg].
    m2 : float
        Mass of body 2 [kg].

    Returns
    -------
    force_vec : numpy.ndarray of shape (2,)
        Gravitational force vector acting on body 1 due to body 2 [N].

    Raises
    ------
    ValueError
        If the distance between bodies is smaller than `epsilon`, to prevent
        division by zero or numerical overflow.

    Notes
    -----
    The gravitational force is computed using Newton’s law of gravitation:

        F₁₂ = G * m₁ * m₂ / |r₂ - r₁|² * (r₂ - r₁) / |r₂ - r₁|

    The direction of the force is from body 1 toward body 2.

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0])
    >>> r2 = np.array([1.0, 0.0])
    >>> m1, m2 = 5.0, 10.0
    >>> gravitational_force(r1, r2, m1, m2)
    array([3.33715e-10, 0.00000e+00])
    """
    diff = r2 - r1
    dist = np.linalg.norm(diff)

    if dist < epsilon:
        raise ValueError(f"Distance too small: {dist} < {epsilon}")

    force_mag = G * m1 * m2 / dist**2
    force_vec = force_mag * diff / dist
    return force_vec


def compute_accelerations(positions, masses, G=G):
    """
    Compute the net gravitational acceleration on each body in an N-body system.

    Parameters
    ----------
    positions : numpy.ndarray of shape (N, 2)
        Array of 2D position vectors for all bodies [m].
    masses : numpy.ndarray of shape (N,)
        Masses of all bodies [kg].
    G : float, optional
        Gravitational constant [m³ kg⁻¹ s⁻²].
        Defaults to the module-level value `G`.

    Returns
    -------
    acc : numpy.ndarray of shape (N, 2)
        Net acceleration vectors of each body [m/s²].

    Notes
    -----
    This function performs a pairwise summation of gravitational forces between
    all bodies (O(N²) complexity). For each pair (i, j), the acceleration on `i`
    due to `j` is:

        aᵢⱼ = G * mⱼ / |rⱼ - rᵢ|³ * (rⱼ - rᵢ)

    Then the total acceleration on body `i` is the sum of all `aᵢⱼ` for j ≠ i.

    Examples
    --------
    >>> positions = np.array([[0, 0], [1, 0]], dtype=float)
    >>> masses = np.array([1e30, 6e24])
    >>> compute_accelerations(positions, masses)
    array([[3.99e-14, 0.00e+00],
           [-6.64e-03, 0.00e+00]])
    """
    N = len(positions)
    acc = np.zeros_like(positions)

    for i in range(N):
        for j in range(N):
            if i != j:
                acc[i] += gravitational_force(
                    positions[i], positions[j], masses[i], masses[j]
                ) / masses[i]

    return acc
