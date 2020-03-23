import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np
years=[2012,2013,2014,2015,2016,2017]
sales=np.random.randint(low=1000,high=10000,size=6)
exp_sales=np.random.randint(1000,10000,6)
plt.yticks([1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
plt.ylim(1,10000)
plt.title("my chart")        
plt.xlabel("label years")
plt.ylabel("label sales")
plt.grid()
plt.scatter(years,exp_sales,color='r')
plt.plot(years,exp_sales,color='r',label='expected sales')
plt.scatter(years,sales,color='b')
plt.plot(years,sales,color='b',label='actual sales')
plt.legend()  # used to display labels
plt.show()