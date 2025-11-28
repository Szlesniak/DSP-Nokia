import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_VECTOR_SIN = (0.12, -3.4, 5.6, -7.8)
AMPL_VECTOR_COS = (8.7, 6.5, 4.3, 2.1)

# CALCULATION
t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = np.sin(t)
carrier_cos = np.cos(t)

amplitudes_sin = []
amplitudes_cos = []

Tx = np.array([])  # empty time vector
for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
    Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos

    # PRESENTATION
    # parameters
    PERIOD_VECTOR_SIZE = 60

    # loading Rx vector from file and..
    Rx = Tx
    # .. ploting it
    ref = np.sin(t)
    ampl = np.dot(Rx, ref) * 2 / PERIOD_VECTOR_SIZE
    amplitudes_sin.append(ampl)

    ref1 = np.cos(t)
    ampl1 = np.dot(Rx, ref1) * 2 / PERIOD_VECTOR_SIZE
    amplitudes_cos.append(ampl1)

    # spliting vector into time slots coresponding to single periods
    # "-1" causes automatic evaluation array seccond dimension

plt.show(block=False)
# presentation
amplitudes_sin = np.array(amplitudes_sin)  # convert list to numpy 1D array
amplitudes_cos = np.array(amplitudes_cos)  # ...
np.set_printoptions(precision=2)  # set numpy array print precision
print(f"amplitudes_sin = {amplitudes_sin}")
print(f"amplitudes_cos = {amplitudes_cos}")
