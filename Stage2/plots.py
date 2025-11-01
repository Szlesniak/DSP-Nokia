import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi/2
PHASE_SHIFT1 = pi/2



# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t + PHASE_SHIFT1)
Shifted = np.sin(t+PHASE_SHIFT)
Ref_mult_Shifted = Ref*Shifted
dot_product = np.sum(Ref_mult_Shifted)

# PLOTS (HINT: use separate plots, not one with grid)
# components
plt.plot(t, Ref, '.-',color = 'b',label='Ref')
plt.plot(t, Shifted, '.-',color = 'g',  label='Shifted')
plt.grid()
plt.title('Components')
plt.legend(['Ref', ' Shifted'])
plt.show()
# multiplication, HINT: use "stem" function for ploting
plt.stem(t,Ref_mult_Shifted, label='Ref_mult_Shifted')
plt.legend()
plt.grid(True)
plt.title('Multiplication')
plt.ylim([-1,1 ])
plt.show()
# print phase shift and dot product value
print(f'phase shift ={PHASE_SHIFT}')
print(f'dot product ={dot_product}')
