import numpy as np
import pytest

from solar_system import (
    gravitational_force,
    compute_accelerations,
    update_positions,
    update_velocities,
    run_simulation,
)

# Global constant used for tests
G = 6.67430e-11

def test_gravitational_force_magnitude():
    """Gravitational force magnitude matches Newton's law."""
    m1, m2 = 1.0, 2.0
    r1, r2 = np.array([0,0]), np.array([1,0])
    f = gravitational_force(m1, m2, r1, r2, G)
    expected = G*m1*m2 / 1**2
    assert np.isclose(np.linalg.norm(f), expected)

def test_gravitational_force_zero_distance():
    """Gravitational force is zero at identical positions (avoid singularity)."""
    f = gravitational_force(1.0, 1.0, np.array([0,0]), np.array([0,0]), G)
    assert np.allclose(f, [0,0])

def test_compute_accelerations_two_body_symmetry():
    """Two equal masses exert equal and opposite accelerations."""
    masses = np.array([1.0, 1.0])
    positions = np.array([[0,0],[1,0]])
    accs = compute_accelerations(positions, masses, G)
    assert np.allclose(accs[0], -accs[1])

def test_update_positions():
    """Positions update correctly with constant velocity."""
    pos = np.array([[0,0]])
    vel = np.array([[1,0]])
    new_pos = update_positions(pos, vel, 1.0)
    assert np.allclose(new_pos, [[1,0]])

def test_update_velocities():
    """Velocities update correctly with constant acceleration."""
    vel = np.array([[0,0]])
    acc = np.array([[1,0]])
    new_vel = update_velocities(vel, acc, 2.0)
    assert np.allclose(new_vel, [[2,0]])

def test_run_simulation_moves_earth():
    """Earth should move in +y direction after several steps."""
    masses = np.array([1.989e30, 5.972e24])
    positions = np.array([[0,0], [1.496e11, 0]])
    velocities = np.array([[0,0], [0,29780]])

    # Run simulation and unpack only what is returned
    # Set record_trajectory=True to get trajectories and CoG
    pos, vel, traj, cog_positions = run_simulation(
        masses, positions, velocities, dt=3600, steps=10, G=G, record_trajectory=True
    )

    # Earth is the second body
    initial_y = positions[1,1]
    final_y = pos[1,1]
    assert final_y > initial_y, "Earth did not move in +y direction"

    # Optional: check that trajectories have correct shape
    assert traj[1].shape == (11, 2), "Trajectory shape is incorrect"

    # Optional: check CoG is computed
    assert cog_positions.shape == (11,2), "CoG positions shape is incorrect"

