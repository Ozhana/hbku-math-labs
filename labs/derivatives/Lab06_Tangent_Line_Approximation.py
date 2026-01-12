import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def fp(x):
    return np.cos(x)

x0 = 1.0
m = fp(x0)
b = f(x0) - m * x0

x = np.linspace(x0 - 2, x0 + 2, 600)
y = f(x)
tangent = m * x + b

# Compare errors near x0
dx = np.linspace(-0.5, 0.5, 200)
true_vals = f(x0 + dx)
tan_vals = m * (x0 + dx) + b
err = np.abs(true_vals - tan_vals)

plt.figure()
plt.plot(x, y, label="f(x)=sin(x)")
plt.plot(x, tangent, label="Tangent at x0=1")
plt.scatter([x0], [f(x0)])
plt.title("Tangent line approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.figure()
plt.plot(dx, err)
plt.title("Approximation error |f(x0+dx) - tangent(x0+dx)|")
plt.xlabel("dx")
plt.ylabel("absolute error")
plt.show()

"""
Lab 06 — Tangent Line Approximation

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
