import numpy as np
#PARAMS
TIME_VECTOR_SIZE = 15

A = 1
B = 1

#CALCULATIONS
t = np.linspace(0, 2*np.pi, TIME_VECTOR_SIZE, endpoint=False)
Sin_A = A*np.sin(t)
Sin_B = B*np.sin(t)
dot = np.dot(Sin_A, Sin_B)

print(f'A = {A}')
print(f'B = {B}')
print(f'dot = {dot:0.2f}')