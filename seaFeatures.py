import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_style("whitegrid")
df=pd.read_csv("market_fact.csv")
'''
sns.distplot(df['Shipping_Cost'])
plt.show()
'''
#subplots 

plt.subplot(2,2,1)
plt.title('sales')
sns.distplot(df['Sales'])
#2nd
plt.subplot(2,2,2)
plt.title('profit')
sns.distplot(df['Profit'])
#3 subplot

plt.subplot(2,2,3)
#plt.title('profit')
sns.distplot(df['Order_Quantity'])
# 4th subplot

plt.subplot(2,2,4)
#plt.title('profit')
sns.distplot(df['Shipping_Cost'])
plt.show()
# box plot