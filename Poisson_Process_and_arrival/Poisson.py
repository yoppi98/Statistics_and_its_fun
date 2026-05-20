import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lamb = 20

x = np.arange(1, 51)
prob = poisson.pmf(x, lamb)

plt.figure(figsize=(8, 5))
plt.bar(x, prob)
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.title("Poisson Distribution with λ = 20")
plt.grid(axis="y", alpha=0.3)
plt.show()