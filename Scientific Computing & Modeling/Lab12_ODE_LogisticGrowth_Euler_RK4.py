import numpy as np
import matplotlib.pyplot as plt

# Logistic growth: dP/dt = r P (1 - P/K)
r = 1.2
K = 100
P0 = 5

T = 10.0
dt = 0.02
t = np.arange(0, T + dt, dt)

def f(P):
    return r * P * (1 - P / K)

# Euler
P_e = np.zeros_like(t)
P_e[0] = P0
for i in range(len(t)-1):
    P_e[i+1] = P_e[i] + dt * f(P_e[i])

# RK4
P_r = np.zeros_like(t)
P_r[0] = P0
for i in range(len(t)-1):
    P = P_r[i]
    k1 = f(P)
    k2 = f(P + 0.5*dt*k1)
    k3 = f(P + 0.5*dt*k2)
    k4 = f(P + dt*k3)
    P_r[i+1] = P + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

plt.figure()
plt.plot(t, P_e, label="Euler")
plt.plot(t, P_r, label="RK4")
plt.title("Logistic growth ODE: Euler vs RK4")
plt.xlabel("t")
plt.ylabel("Population P(t)")
plt.legend()
plt.show()

"""
Lab 12 — Logistic Growth Euler

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
