import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# modulation
Carrier = np.sin(t)

Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx, amp * Carrier)

# channel
Rx=Tx # ideal one
RxPeriods = np.reshape(Rx, (5, 60))
# demodulation

amplitudes_l = []  # create amplitude list
for RxPeriod in RxPeriods:
    # decode amplitude and append it to list
    # use as many code rows as you need
    t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)
    Ref = np.sin(t)
    dot = np.dot(Ref, RxPeriod)
    ampl = float(2 / TIME_VECTOR_SIZE * dot)
    amplitudes_l.append(round(ampl,2))

# PRESENTATION

# Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

#
print(f'received amplitudes: {amplitudes_l}')


