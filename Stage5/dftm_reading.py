import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from mylib import *

# loads samples from .wav file with exemplary DTFM signal
# adapt file path
samples = read(r'wav\d.wav') #b, c, d
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]
# plt.plot(samples)
# plt.show()
freqs = np.linspace(0,samplig_freq,len(samples))

real, imag = myDFT(samples)
real_amplitudes = np.abs(real)
imag_amplitudes = np.abs(imag)

amplitudes = np.sqrt(real_amplitudes**2 + imag_amplitudes**2)
plt.plot(freqs, amplitudes,label='d.wav')
plt.grid()
plt.legend()


#culd be usefool for zooming
plt.xlim(600,1700)
plt.ylim(-30_000,3_0000)

plt.show()




