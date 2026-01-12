import numpy as np

def f(x):
    return np.exp(-x**2)

def trap(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return dx * (0.5*y[0] + y[1:-1].sum() + 0.5*y[-1])

def simpson(f, a, b, n):
    # n must be even
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return (dx/3) * (y[0] + y[-1] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum())

a, b = 0.0, 1.0

for n in [10, 20, 50, 100, 200]:
    t = trap(f, a, b, n)
    s = simpson(f, a, b, n)
    print(f"n={n:3d}  trapezoid={t:.10f}  simpson={s:.10f}")

print("\nNote: exact value is related to erf(1). Here we compare methods' stability.")


"""
Lab 09 — Numerical Integration Trapezoid Simpson

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
