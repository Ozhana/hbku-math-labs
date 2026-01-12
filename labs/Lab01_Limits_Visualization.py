import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2 - 1) / (x - 1)

x1 = np.linspace(0.0, 0.98, 300)
x2 = np.linspace(1.02, 2.0, 300)

plt.figure()
plt.plot(x1, f(x1), label="f(x)=(x^2-1)/(x-1)")
plt.plot(x2, f(x2))
plt.axvline(1, linestyle="--")
plt.title("Limit Visualization: removable discontinuity at x=1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
