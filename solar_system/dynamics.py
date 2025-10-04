import numpy as np

G = 6.67430e-11
epsilon = 1e-6

def gravitational_force(r1, r2, m1, m2):
    diff = r2 - r1
    dist = np.linalg.norm(diff)
    if dist < epsilon:
        raise ValueError(f"Distance too small: {dist} < {epsilon}")
    force_mag = G * m1 * m2 / dist**2
    force_vec = force_mag * diff / dist
    return force_vec

def compute_accelerations(positions, masses, G):
    N = len(positions)
    acc = np.zeros_like(positions)
    for i in range(N):
        for j in range(N):
            if i != j:
                acc[i] += gravitational_force(positions[i], positions[j], masses[i], masses[j]) / masses[i]
    return acc
