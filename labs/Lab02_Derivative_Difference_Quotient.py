import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

x0 = 1.0
hs = np.logspace(-1, -8, 50)
approx = (f(x0 + hs) - f(x0)) / hs
true = 3 * x0**2

plt.figure()
plt.semilogx(hs, np.abs(approx - true))
plt.gca().invert_xaxis()
plt.title("Derivative by Difference Quotient: error vs step size")
plt.xlabel("h")
plt.ylabel("|approx - true|")
plt.show()
