import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np
x=[1,2,3,4,5,6,7,8,9,10]
y=np.random.randint(10,1000,10)
c=['a','b','c','d','e','f','g','h','i','j']
#plt.scatter(x,y,s=y,marker='$1$') # to plot diff sizes set s=y, for chnging marker we use 
for i in range(0,len(x)):
    plt.scatter(x[i],y[i],s=y[i],marker='$'+c[i]+'$')
plt.show()