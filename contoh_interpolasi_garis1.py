import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6])
y = np.array([0,0.9,1,0.15,-0.8,-1,-0.2])
sumbux = 0*x

plt.plot(x,y,'ro',x,y,x,sumbux,'k-|')
plt.show()