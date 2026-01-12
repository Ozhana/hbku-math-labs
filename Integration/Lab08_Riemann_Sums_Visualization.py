import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 1

a, b = 0.0, 2.0
n = 10  # try 10, 20, 50, 100

x = np.linspace(a, b, 600)
y = f(x)

# Midpoint Riemann sum
edges = np.linspace(a, b, n+1)
mid = (edges[:-1] + edges[1:]) / 2
dx = (b - a) / n
approx = np.sum(f(mid) * dx)

plt.figure()
plt.plot(x, y, label="f(x)=x^2+1")
for i in range(n):
    left = edges[i]
    right = edges[i+1]
    height = f((left + right) / 2)
    plt.plot([left, left, right, right], [0, height, height, 0])
plt.title(f"Midpoint Riemann Sum, n={n}, approx={approx:.6f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# exact integral: ∫(x^2+1) dx from 0 to 2 = [x^3/3 + x]_0^2 = 8/3 + 2 = 14/3
exact = 14/3
print(f"Approx = {approx:.8f}, Exact = {exact:.8f}, Error = {abs(approx-exact):.8f}")

"""
Lab 08 — Lab08 Riemann Sums Visualization

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
