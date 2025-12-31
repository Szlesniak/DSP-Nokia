import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot, myDFT

SAMPLE_NR = 10

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.cos(t*1)*2/5 + np.sin(t*4)*4/5
my_stem_plot(samples,f'samples')

real, imag = myDFT(samples)
my_stem_plot(real,'my DFT real',y_range=(-6,7))
my_stem_plot(imag,'my DFT imag',y_range=(-6,7))

fft = np.fft.fft(samples)
my_stem_plot(fft.real,'FFT real',y_range=(-6,7))
my_stem_plot(fft.imag,'FFT imag',y_range=(-6,7))