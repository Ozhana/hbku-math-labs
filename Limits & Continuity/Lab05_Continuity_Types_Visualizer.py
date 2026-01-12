import numpy as np
import matplotlib.pyplot as plt

def g(x):
    # piecewise: jump + removable examples combined
    y = np.where(x < 0, x + 1, 2 - x)  # jump at x=0
    return y

def h(x):
    # removable at x=1 (same as simplified x+1 except hole)
    return (x**2 - 1) / (x - 1)

def local_limits(func, a, deltas):
    left = func(a - deltas)
    right = func(a + deltas)
    return left[-1], right[-1]  # smallest delta values

deltas = np.logspace(-2, -12, 50)

# Plot g (jump)
x = np.linspace(-2, 2, 800)
plt.figure()
plt.plot(x, g(x), label="g(x) = x+1 (x<0), 2-x (x>=0)")
plt.axvline(0, linestyle="--")
gl, gr = local_limits(g, 0.0, deltas)
plt.title(f"Jump discontinuity at x=0 (approx limits L={gl:.3f}, R={gr:.3f})")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.show()

# Plot h (removable)
x1 = np.linspace(-1, 0.99, 600)
x2 = np.linspace(1.01, 3, 600)
plt.figure()
plt.plot(x1, h(x1), label="h(x)=(x^2-1)/(x-1)")
plt.plot(x2, h(x2))
plt.axvline(1, linestyle="--")
hl, hr = local_limits(h, 1.0, deltas)
plt.scatter([1], [2.0], marker="o")  # limit value
plt.title(f"Removable discontinuity at x=1 (approx limits L={hl:.3f}, R={hr:.3f})")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()
plt.show()

"""
Lab 05 — Continuity Types Visualizer

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
