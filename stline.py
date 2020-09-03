' Matrix Theory : Assignment 1 : Shantanu Yadav : EE20MTECH12001'
'Problem Statement : Find the equations of the lines which have intercepts on'
'on axes whose sum and product are 1 and -6 respectively.'
'The intercepts are solved using the two equations a+ b =1 a*b=-6'
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

axes = plt.gca()
plt.grid()
x_vals = np.arange(-8,5,1)
y_vals = 3 +1.5 * x_vals
y_vals1 = -2 +0.667 *  x_vals
line,=plt.plot(x_vals, y_vals,'b-')
line.set_label('y = 1.5x + 3')
line_2,=plt.plot(x_vals,y_vals1,'r-' )
line_2.set_label('y = 0.667x - 2')
plt.xticks(np.arange(min(x_vals), max(x_vals)+1, 1.0))
plt.yticks(np.arange(min(y_vals), max(y_vals)+1, 1.0))
plt.legend()


plt.plot(3,0,'o-',0,-2,'o-')
plt.annotate("(3,0)",(3,0))
plt.annotate("(0,-2)",(0,-2))
plt.plot(-2,0,'o-',0,3,'o-')
plt.annotate("(-2,0)",(-2,0))
plt.annotate("(0,3)",(0,3))
    


