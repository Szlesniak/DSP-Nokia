import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

pi = np.pi

t = np.linspace(0, 4*2*pi,60, endpoint=False)
sin = -1.6*np.sin(t)
saw = 2.8*signal.sawtooth(t, 0.5)

sum = sin + saw

plt.plot(t,sin, 'p', label='sin', color='blue')
plt.plot(t,saw, '-p', label='saw', color='green')
plt.plot(t,sum,'--', label='sum', color='brown')
plt.title('triangle + sinus')
plt.ylabel('amplitudo[a.u.]')
plt.xlabel('tempus[s]')
plt.ylim(-4,6)
plt.xlim(0,10)

plt.grid()
plt.legend()
plt.show()

