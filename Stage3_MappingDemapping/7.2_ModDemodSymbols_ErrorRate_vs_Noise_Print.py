import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol
import random
# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
NOISE_NUMBERS = 10
NOISE_DEVIATION = list()
for i in range(NOISE_NUMBERS):
    NOISE_DEVIATION.append(round(random.uniform(i, i+1)/NOISE_NUMBERS*2, 2))

SYMBOL_NR = 8
print(f'SYMBOL_NR: {SYMBOL_NR}')
t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Ref = Carrier
print("noise dev: error nr")
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
    print(f'{noise}: {sum(symbols_rx != symbols_tx)}')
# PRESENTATION





