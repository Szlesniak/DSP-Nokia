import matplotlib.pyplot as plt
import numpy as np

pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
NUMBEER_OF_AMPLITUDES = 8
AMPL_VECTOR = np.linspace(0.5, 4, NUMBEER_OF_AMPLITUDES, endpoint=True)
ampls = []
amp_max = 4
amp_min = 0.5
NOISE_DEVIATION = round((amp_max - amp_min) / (2 * (len(AMPL_VECTOR) - 1)), 2)
TRANSMISION_NR = 100
for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i % 8]
    # CALCULATION
    t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)
    # modulation
    Carrier = np.sin(t)

    Tx = amp * Carrier
    noise = np.random.normal(0, NOISE_DEVIATION, TIME_VECTOR_SIZE)
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

    # PRESENTATION

amplitudes = np.array(ampls)
colors = ["red", "orange", "green", "blue", "purple", "brown", "gray", "black"]

for k in range(8):
    plt.plot(amplitudes[k::8], "p", color=colors[k])
plt.axhline(y=0, color="black")
plt.grid(axis="y")
plt.show()
print(f"NOISE_DEVIATION={NOISE_DEVIATION}")
