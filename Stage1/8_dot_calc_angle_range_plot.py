from mylib import rotate_vector
from matplotlib import pyplot as plt
import numpy as np
v = np.array([0, 1])


angle_list = list() #create empty list
dot_list = list()       #create empty list

for angle in range(0,361):
    angle_list.append(angle)
    v_rot = rotate_vector(v, angle) #see examp. from prev. slide
    dot = np.dot(v, v_rot)
    dot_list.append(dot)

plt.plot(angle_list,dot_list)

plt.xlabel("angle")
plt.ylabel("dot")

plt.grid()
plt.show()



