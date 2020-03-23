import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np

x=np.random.randint(100,1000,10)
explode=[0,0,0,0,0.5,0,0.2,0,0.6,0]
#plt.pie(x,explode=explode,autopct="%.2f%%") #jis format m show krna hai ,.2f is for 2 decimal places,to print % type 2 times %
labels=['a','b','c','d','e','f','g','h','i','j']
plt.pie(x,labels=labels)                      #to print labels on pie
plt.show()                                           
