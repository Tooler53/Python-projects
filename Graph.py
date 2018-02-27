import numpy as np 
import matplotlib.pyplot as plt 

pi = np.pi
e = np.e

def f(t):
    return pow (e, ((pow (t,2)/pi)*-1))

x = []; y = []
i = -10

while i<11:
    x.append(i)
    y.append (f(i))
    i+=1

plt.plot(x,y)
print ('x - '+str(x))
print ('y - '+str(y))
plt.show()