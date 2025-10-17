import numpy as np
from mylib import rotate_vector
green = [0,1]
blue = [0,1]

# green_length = np.sqrt(green[0]**2+green[1]**2)
# blue_length = np.sqrt(blue[0]**2 + blue[1]**2)
# for i in range(0,370,10):
#     print(f'{i:03d}: {float(green_length*blue_length*np.cos(2*np.pi*i/360)) :+0.3f}')

for i in range(0,370,10):
    blue_rot = rotate_vector(blue,i)
    print(f'{i:03d}: {np.dot(green,blue_rot):+0.3f}')


