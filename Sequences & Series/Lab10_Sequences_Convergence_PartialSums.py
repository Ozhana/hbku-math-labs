import numpy as np
import matplotlib.pyplot as plt

N = 200

# sequences (terms)
n = np.arange(1, N+1)
a1 = 1/n                 # harmonic terms
a2 = 1/(n**2)            # p-series terms
a3 = (0.8)**n            # geometric terms

# partial sums (series)
S1 = np.cumsum(a1)       # diverges
S2 = np.cumsum(a2)       # converges
S3 = np.cumsum(a3)       # converges

plt.figure()
plt.plot(n, S1, label="Σ 1/n (diverges)")
plt.plot(n, S2, label="Σ 1/n^2 (converges)")
plt.plot(n, S3, label="Σ (0.8)^n (converges)")
plt.title("Partial sums: convergence vs divergence")
plt.xlabel("N")
plt.ylabel("S_N")
plt.legend()
plt.show()

"""
Lab 10 — Sequences Convergence PartialSums

Tools: Python, NumPy, Matplotlib
Author: Ozhan Akdag
"""
