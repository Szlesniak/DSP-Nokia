import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
ampls = []
errors = []
for amp in AMPL_VECTOR:
    # CALCULATION
    t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)
    # modulation
    Carrier = np.sin(t)

    Tx = amp * Carrier
    noise = np.random.normal(0, 1, TIME_VECTOR_SIZE)
    Tx = Tx + noise

    # channel
    Rx = Tx
    # demodulation
    # decode amplitude and append it to list
    # use as many code rows as you need
    Ref = np.sin(t)
    dot = np.dot(Ref, Rx)
    ampl = float(2 / TIME_VECTOR_SIZE * dot)
    ampls.append(ampl)
    errors.append(ampl - amp)

    # PRESENTATION
    #   Tx plot
    plt.plot(Tx)
    plt.axhline(y=0, color="black")
    plt.grid(axis="y")
    plt.show()

print(f"received amplitudes: {ampls}")
print(f"errors: {errors}")
