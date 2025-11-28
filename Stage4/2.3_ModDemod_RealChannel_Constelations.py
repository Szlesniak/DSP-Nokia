import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_VECTOR_SIN = (1, -1, 1, -1)
AMPL_VECTOR_COS = (1, 1, -1, -1)

# CALCULATION
t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = np.sin(t)
carrier_cos = np.cos(t)

amplitudes_sin = []
amplitudes_cos = []
NOISE_DEVIATION = 0.5
TRANSMISSON_NR = 10
for i in range(TRANSMISSON_NR):
    for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
        Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos

        # PRESENTATION
        # parameters
        PERIOD_VECTOR_SIZE = 60
        noise = np.random.normal(0, NOISE_DEVIATION, PERIOD_VECTOR_SIZE)
        # loading Rx vector from file and..
        Rx = Tx + noise
        # .. ploting it
        ref = np.sin(t)
        ampl = np.dot(Rx, ref) * 2 / PERIOD_VECTOR_SIZE
        amplitudes_sin.append(ampl)

        ref1 = np.cos(t)
        ampl1 = np.dot(Rx, ref1) * 2 / PERIOD_VECTOR_SIZE
        amplitudes_cos.append(ampl1)
    plt.scatter(amplitudes_sin, amplitudes_cos, color="blue")
    plt.grid(True)
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    # spliting vector into time slots coresponding to single periods
    # "-1" causes automatic evaluation array seccond dimension
plt.title("RX amplitudes")
plt.show()
# presentation amplitudes_sin = np.array(amplitudes_sin)  # convert list to numpy 1D array
