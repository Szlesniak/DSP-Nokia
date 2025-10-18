import numpy as np

sig1 = [0.088,0.088,0.088,0.442,0.530,0.000,-0.530,-0.442,-0.088,-0.088,-0.088]

sig2 = [0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500, 0.350, 0.500, 0.650, 0.500]
dot_numbers = []
for i in range(0,len(sig1)):
    dot_numbers.append(sig1[i]*sig2[i])
dot_product = np.sum(dot_numbers)
print(dot_product)
