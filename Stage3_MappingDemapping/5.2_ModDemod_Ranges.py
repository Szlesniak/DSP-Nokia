import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
ampls = []
errors = []
NOISE_DEVIATION=0.5
TRANSMISION_NR = 100
for i in range (TRANSMISION_NR):
    amp = AMPL_VECTOR[i%4]
    # CALCULATION
    t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

    # modulation
    Carrier = np.sin(t)

    Tx = amp * Carrier
    noise = np.random.normal(0,NOISE_DEVIATION,TIME_VECTOR_SIZE)
    Tx = Tx + noise

    # channel
    Rx= Tx

    # demodulation



    # decode amplitude and append it to list
    # use as many code rows as you need
    #t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)
    Ref = np.sin(t)
    dot = np.dot(Ref, Rx)
    ampl = float(2 / TIME_VECTOR_SIZE * dot)
    ampls.append(ampl)

    # PRESENTATION

    #   Tx plot
    # plt.plot(Tx)
    # plt.axhline(y=0,color='black')
    # plt.grid(axis='y')
    # plt.show()

    #

plt.plot(ampls, '.',markersize=12)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()


