import numpy as np
import matplotlib.pyplot as plt

"""
HBKU Computational Lab: Numerical Integration Benchmark
Researcher: Dr. Ozhan Akdag
Goal: Compare Riemann Sums vs. Simpson's Rule for complex functions.
"""

def target_function(x):
    return np.sin(x)**2 + x * np.cos(x)

def showcase_analysis():
    a, b = 0, 10  # Integration limits
    n = 100       # Subdivisions
    x = np.linspace(a, b, n)
    y = target_function(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'r', weight='bold', label='f(x) = sin²(x) + x·cos(x)')
    plt.fill_between(x, y, alpha=0.2, color='red', label='Area under curve')
    
    plt.title("Computational Mathematics: Area Estimation", fontsize=14)
    plt.xlabel("Domain (x)")
    plt.ylabel("Codomain (f(x))")
    plt.legend()
    plt.grid(True, linestyle='--')
    
    # Save for GitHub README
    plt.savefig('integration_demo.png')
    print("[+] Integration plot saved as 'integration_demo.png'")

if __name__ == "__main__":
    showcase_analysis()
