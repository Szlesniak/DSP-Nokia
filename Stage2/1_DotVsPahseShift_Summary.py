import numpy as np
import matplotlib.pyplot as plt

shift = np.arange(0, np.pi, np.pi / 16)
t = np.linspace(0, 2 * np.pi, 30, endpoint=False)
dots = []

for i in shift:
    sin1 = np.sin(t)
    sin2 = np.sin(t + i)
    dots.append(np.sum(sin1 * sin2))
plt.plot(shift, dots, ".-", color="blue", label="dot(shift)")
plt.grid()
plt.legend()
plt.show()
