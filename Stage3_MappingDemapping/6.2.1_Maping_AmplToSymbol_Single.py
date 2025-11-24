import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl
from mapper_lib import ampl_to_symbol

for symbol_nr in 2, 4, 8:
    symbols_l = list()
    ampl_l = np.linspace(-1.5, 1.5, 100)
    for ampl in ampl_l:
        symbol = ampl_to_symbol(symbol_nr, ampl)
        symbols_l.append(symbol)
    plt.plot(ampl_l, symbols_l, 'p-', label=f'symbol nr = {symbol_nr}')


plt.legend()
plt.grid()
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.show()