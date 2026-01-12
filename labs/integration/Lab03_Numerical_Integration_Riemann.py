import numpy as np

def riemann_sum(f, a, b, n):
    x = np.linspace(a, b, n+1)
    mid = (x[:-1] + x[1:]) / 2
    dx = (b - a) / n
    return np.sum(f(mid) * dx)

f = lambda x: np.sin(x)

a, b = 0, np.pi
for n in [10, 50, 200, 1000]:
    approx = riemann_sum(f, a, b, n)
    print(f"n={n:4d}  approx={approx:.8f}")

print("True integral of sin(x) from 0 to pi is 2.")

"""
Lab 03 — Numerical Integration Riemann

Tools: Python, NumPy, Matplotlib
Author: Dr.Ozhan Akdag
"""
