import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # removable discontinuity example: (x^2 - 1)/(x - 1) for x != 1, define f(1)=0
    y = (x**2 - 1) / (x - 1)
    return y

def estimate_limit(func, a, deltas):
    # estimate left/right limits numerically
    left_vals = func(a - deltas)
    right_vals = func(a + deltas)
    return left_vals, right_vals

a = 1.0
deltas = np.logspace(-1, -10, 10)

left, right = estimate_limit(f, a, deltas)

print("Estimating limit of f(x)=(x^2-1)/(x-1) as x -> 1")
print("delta        f(1-delta)       f(1+delta)")
for d, lv, rv in zip(deltas, left, right):
    print(f"{d:1.0e}      {lv: .10f}      {rv: .10f}")

# Plot around the point
x1 = np.linspace(0.0, 0.99, 400)
x2 = np.linspace(1.01, 2.0, 400)

plt.figure()
plt.plot(x1, f(x1), label="f(x)=(x^2-1)/(x-1)")
plt.plot(x2, f(x2))
plt.axvline(a, linestyle="--")
plt.scatter([a], [2.0], marker="o")   # the limit value
plt.title("Numerical limit checks near x=1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

"""
Lab 04 — Limit Numerical Checks

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
