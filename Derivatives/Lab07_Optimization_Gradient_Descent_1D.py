import numpy as np
import matplotlib.pyplot as plt

# Minimize a function using gradient descent (1D)
def f(x):
    return (x - 2)**2 + 0.5*np.sin(5*x)

def grad(x, h=1e-6):
    # numerical derivative
    return (f(x + h) - f(x - h)) / (2*h)

x = 0.0          # start point
alpha = 0.05     # step size
steps = 60

xs = [x]
fs = [f(x)]

for _ in range(steps):
    x = x - alpha * grad(x)
    xs.append(x)
    fs.append(f(x))

xs = np.array(xs)
fs = np.array(fs)

# Plot function and steps
grid = np.linspace(-1, 4, 800)
plt.figure()
plt.plot(grid, f(grid), label="f(x)")
plt.scatter(xs, fs, s=20, label="iterations")
plt.title("Gradient Descent (1D) for optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

print(f"Final x ≈ {xs[-1]:.6f}, f(x) ≈ {fs[-1]:.6f}")

"""
Lab 07 — Optimization Gradient Descent

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
