import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
for amp in AMPL_VECTOR:

    # CALCULATION
    t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

    # modulation
    Carrier = np.sin(t)

    Tx = amp * Carrier

    # channel
    Rx=Tx # ideal one

    # demodulation



    # decode amplitude and append it to list
    # use as many code rows as you need
    #t = np.linspace(0, 2 * pi, TIME_VECTOR_SIZE, endpoint=False)
    Ref = np.sin(t)
    dot = np.dot(Ref, Rx)
    ampl = round(float(2 / TIME_VECTOR_SIZE * dot),2)


    # PRESENTATION

    #   Tx plot
    plt.plot(Rx)
    plt.axhline(y=0,color='black')
    plt.grid(axis='y')
    plt.show()

    #
    print(f'received amplitude: {ampl}')


