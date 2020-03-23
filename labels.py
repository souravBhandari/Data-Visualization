import matplotlib.pyplot as plt 
from matplotlib import style
x=[1,2,3,4,5]
y=[2,3,4,5,6]
style.use('dark_background')# if want to add dark bakground .style is customization
plt.title("my chart")        # all pyplot attributes -> xlabels,ylabels,chart grid
plt.xlabel("label x")
plt.ylabel("label y")
plt.grid()
plt.xticks([0,2,4,6,8])
plt.xlim(1,10) # limits the x axis limit
plt.yticks([0,2,4,6,8])  # y axis values
plt.ylim(1,10)        # y axis limit
plt.plot(x,y)
plt.show()
