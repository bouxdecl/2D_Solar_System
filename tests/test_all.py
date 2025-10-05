import numpy as np
import pytest

from solar_system.dynamics import gravitational_force, compute_accelerations
from solar_system.planets import get_planets, PLANETS
from solar_system.integration import euler_step, rk4_step

# --- Dynamics tests ---

def test_gravitational_force_magnitude():
    r1 = np.array([0.0, 0.0])
    r2 = np.array([1.0, 0.0])
    f = gravitational_force(r1, r2, 1.0, 1.0)
    expected = 6.67430e-11  # G * m1 * m2 / r^2
    assert np.allclose(np.linalg.norm(f), expected)

def test_gravitational_force_zero_distance():
    r1 = np.array([0.0, 0.0])
    r2 = np.array([0.0, 0.0])
    with pytest.raises(ValueError):
        gravitational_force(r1, r2, 1.0, 1.0)

def test_compute_accelerations_two_body_symmetry():
    positions = np.array([[0.0, 0.0], [1.0, 0.0]])
    masses = np.array([1.0, 1.0])
    acc = compute_accelerations(positions, masses, G=6.67430e-11)
    # accelerations should be equal in magnitude and opposite
    assert np.allclose(acc[0], -acc[1])
    assert np.isclose(np.linalg.norm(acc[0]), np.linalg.norm(acc[1]))

# --- Planets tests ---

def test_get_planets_output_shapes():
    names, masses, positions, velocities = get_planets(3)
    assert len(names) == 3
    assert masses.shape == (3,)
    assert positions.shape == (3, 2)
    assert velocities.shape == (3, 2)

def test_get_planets_positions_and_velocities():
    names, masses, positions, velocities = get_planets(2)
    # Sun at origin
    assert np.allclose(positions[0], [0, 0])
    # Planets on x-axis, velocities along y
    for i in range(1, 2):
        assert positions[i][1] == 0.0
        assert velocities[i][0] == 0.0
        assert velocities[i][1] > 0.0

# --- Integration tests ---

def test_euler_step_basic_motion():
    positions = np.array([[0.0, 0.0]])
    velocities = np.array([[1.0, 0.0]])
    masses = np.array([1.0])
    dt = 0.1
    new_pos, new_vel = euler_step(positions, velocities, masses, dt, G=6.67430e-11)
    # Should move roughly in x direction
    assert new_pos[0][0] > positions[0][0]
    assert new_pos[0][1] == positions[0][1]

def test_rk4_step_basic_motion():
    positions = np.array([[0.0, 0.0]])
    velocities = np.array([[1.0, 0.0]])
    masses = np.array([1.0])
    dt = 0.1
    new_pos, new_vel = rk4_step(positions, velocities, masses, dt, G=6.67430e-11)
    assert new_pos[0][0] > positions[0][0]
    assert new_pos[0][1] == positions[0][1]

def test_rk4_vs_euler_small_dt():
    positions = np.array([[0.0, 0.0]])
    velocities = np.array([[1.0, 0.0]])
    masses = np.array([1.0])
    dt = 1e-6
    pos_euler, _ = euler_step(positions, velocities, masses, dt, G=6.67430e-11)
    pos_rk4, _ = rk4_step(positions, velocities, masses, dt, G=6.67430e-11)
    # With tiny dt, RK4 and Euler should be nearly equal
    assert np.allclose(pos_euler, pos_rk4, rtol=1e-8, atol=1e-12)
