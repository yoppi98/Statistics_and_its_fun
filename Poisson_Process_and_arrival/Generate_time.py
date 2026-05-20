import numpy as np
import matplotlib.pyplot as plt


lamb = 1


Tmax = 50

waiting_times = []
current_time = 0

while current_time < Tmax:
    u = np.random.rand()
    waiting_time = -(1 / lamb) * np.log(1 - u)
    current_time += waiting_time
    if current_time < Tmax:
        waiting_times.append(waiting_time)

arrival_times = np.cumsum(waiting_times)

plt.figure(figsize=(10, 5))

for t in arrival_times:
    plt.vlines(t, 0, 1)

plt.xlabel("time")
plt.ylabel("arrival event")
plt.title("Simulated Arrival Times in a Poisson Process")
plt.ylim(-0.05, 1.05)
plt.grid(alpha=0.3)
plt.show()