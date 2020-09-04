#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:10:04 2020

@author: shantanu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:21:59 2020

@author: shantanu
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
fig.set_size_inches(10,10)
ax = fig.add_subplot(111, projection='3d')

x_1=np.array([-4,16])
y_1=np.array([22,-18])
z_1=np.array([-18,22])

x_2=np.array([-34,26])
y_2=np.array([20,-20])
z_2=np.array([19,-21])

line_1,=ax.plot(x_1,y_1,z_1,color='red',label="line 1")
line_1.set_label('line 1')
ax.plot(x_2,y_2,z_2,color='blue')



a=np.array([[-9,5],[-5,17]])
b=np.array([8,24]).reshape(2,1)

x=np.linalg.solve(a,b)

lambda_1 = x[0]
lambda_2 = x[1]

a_1 = np.array([6,2,2]).reshape(3,1)
b_1= np.array([1,-2,2]).reshape(3,1)
P = a_1 + lambda_1*b_1

a_2 = np.array([-4,0,-1]).reshape(3,1)
b_2= np.array([3,-2,-2]).reshape(3,1)
Q = a_2 + lambda_2*b_2

print("Point P is : " , P.reshape(1,3))

print("The point Q is: ",Q.reshape(1,3))

pointx = np.array([Q[0],P[0]])
pointy = np.array([Q[1],P[1]])
pointz = np.array([Q[2],P[2]])


ax.scatter(pointx,pointy,pointz,s=50)


ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('Skew lines and the shortest distance points')


ax.text(5.875,2.25,1.75,'point P') 
ax.text(0.125,-2.75,-3.75,'point Q') 

plt.show()
