import matplotlib.pyplot as plt
import numpy as np

from mapper_lib import ampl_to_symbol, symbol_to_ampl

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATION = (0.00, 0.22, 0.44, 0.67, 0.89, 1.11, 1.33, 1.56, 1.78, 2.00)
SYMBOL_NR = 8
print(f"SYMBOL_NR: {SYMBOL_NR}")
print("DEV: SIN, COS")
t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t)
carrier_cos = ref_cos = np.cos(t)

# TRANSMISION-RECEPTION


symbols_tx_sin = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)
symbols_tx_cos = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)
for noise in NOISE_DEVIATION:
    errors_sin = list()
    errors_cos = list()
    symbols_rx_sin = list()
    symbols_rx_cos = list()
    for symbol_sin, symbol_cos in zip(symbols_tx_sin, symbols_tx_cos):
        # modulation
        ampl_sin = symbol_to_ampl(SYMBOL_NR, symbol_sin)
        ampl_cos = symbol_to_ampl(SYMBOL_NR, symbol_cos)
        Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos
        # real channel
        Rx = Tx + np.random.normal(loc=0, scale=noise, size=len(Tx))
        # demodulation
        ampl_sin = np.dot(Rx, ref_sin) * 2 / TIME_VECTOR_SIZE
        ampl_cos = np.dot(Rx, ref_cos) * 2 / TIME_VECTOR_SIZE

        symbol_sin = ampl_to_symbol(SYMBOL_NR, ampl_sin)
        symbol_cos = ampl_to_symbol(SYMBOL_NR, ampl_cos)

        symbols_rx_sin.append(symbol_sin)
        symbols_rx_cos.append(symbol_cos)
    errors_sin = np.sum(symbols_rx_sin != symbols_tx_sin)
    errors_cos = np.sum(symbols_rx_cos != symbols_tx_cos)

    print(f"{noise} : {errors_sin}, {errors_cos}")
# PRESENTATION
