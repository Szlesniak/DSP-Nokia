import numpy as np
from matplotlib import pyplot as plt


def my_stem_plot(y, title, y_range=None):
    x = np.arange(len(y))
    plt.stem(x, y, '-p')

    plt.xticks(x)

    if y_range:
        plt.ylim(y_range)
        plt.yticks(np.arange(*y_range))

    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()

def myDFT(samples):
    real = list()
    imag = list()
    t = np.linspace(0,2*np.pi,len(samples),endpoint=False)
    for f in range(len(t)):
        real.append(np.dot(np.cos(t*f),samples))
        imag.append(np.dot(-np.sin(t*f),samples))
    return real, imag