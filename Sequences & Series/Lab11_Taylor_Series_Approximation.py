import numpy as np
import matplotlib.pyplot as plt

def taylor_sin(x, terms):
    # sin(x) = Σ (-1)^k x^(2k+1)/(2k+1)!
    s = 0.0
    fact = 1.0
    power = x
    sign = 1.0
    for k in range(terms):
        # compute (2k+1)! incrementally
        if k == 0:
            fact = 1.0
            power = x
        else:
            # update power x^(2k+1) from previous x^(2k-1)
            power *= x*x
            # update factorial from (2k-1)! to (2k+1)!
            fact *= (2*k)*(2*k+1)
        s += sign * power / fact
        sign *= -1
    return s

x = np.linspace(-np.pi, np.pi, 800)
true = np.sin(x)

plt.figure()
plt.plot(x, true, label="sin(x)")

for terms in [1, 2, 3, 5, 8]:
    approx = np.array([taylor_sin(xi, terms) for xi in x])
    plt.plot(x, approx, label=f"{terms} terms")

plt.title("Taylor approximation to sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

"""
Lab 11 — Taylor Series Approximation

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
