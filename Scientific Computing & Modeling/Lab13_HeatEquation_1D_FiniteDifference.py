import numpy as np
import matplotlib.pyplot as plt

# 1D heat equation: u_t = alpha * u_xx on x in [0,1]
alpha = 0.01
Nx = 120
dx = 1.0 / (Nx - 1)
x = np.linspace(0, 1, Nx)

# stability condition for explicit method: dt <= dx^2/(2*alpha)
dt = 0.4 * dx*dx / (2*alpha)
T = 1.0
Nt = int(T / dt)

# initial condition: a "hot bump"
u = np.exp(-200*(x-0.3)**2)

def step(u):
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + alpha * dt / (dx*dx) * (u[2:] - 2*u[1:-1] + u[:-2])
    # boundary conditions: fixed at 0
    u_new[0] = 0
    u_new[-1] = 0
    return u_new

plt.figure()
plt.plot(x, u, label="t=0")

snapshots = [0.1, 0.3, 0.6, 1.0]
snapshot_steps = [int(s / dt) for s in snapshots]

for n in range(1, Nt+1):
    u = step(u)
    if n in snapshot_steps:
        plt.plot(x, u, label=f"t={n*dt:.2f}")

plt.title("1D Heat equation (explicit finite difference)")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.show()

"""
Lab 13 — Heat Equation Finite Difference

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
