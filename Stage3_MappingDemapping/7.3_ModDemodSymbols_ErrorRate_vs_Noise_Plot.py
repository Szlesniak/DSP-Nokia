import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol
import random
# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
NOISES_NUMBER = 20
NOISE_DEVIATION = list()
# NOISE_DEVIATION = np.array([0.00,0.22,0.44,0.67,0.89,1.11,1.33,1.56,1.78,2.00])
for i in range(NOISES_NUMBER):
    NOISE_DEVIATION.append(round(random.uniform(i, i+1)/NOISES_NUMBER*5, 2))

for SYMBOL_NR in 2,4,8:

    t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
    Carrier = np.sin(t)
    Ref = Carrier

    # TRANSMISION-RECEPTION
    symbols_tx = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)

    errors = list()
    for noise in NOISE_DEVIATION:
        symbols_rx = list()
        for symbol in symbols_tx:
            # modulation
            ampl = symbol_to_ampl(SYMBOL_NR, symbol)
            Tx = ampl * Carrier
            # real channel
            Rx = Tx + np.random.normal(0, noise, TIME_VECTOR_SIZE)
            # demodulation
            ampl = (np.dot(Rx, Ref) / TIME_VECTOR_SIZE) * 2
            symbol = ampl_to_symbol(SYMBOL_NR, ampl)
            symbols_rx.append(symbol)
        errors.append(sum(symbols_rx != symbols_tx))
    plt.plot(NOISE_DEVIATION, errors,'p-', label=f'symbol nr = {SYMBOL_NR}')
# PRESENTATION
plt.grid(True)
plt.legend()
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.show()




