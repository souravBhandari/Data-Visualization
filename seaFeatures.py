import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_style("whitegrid")
<<<<<<< HEAD
df=pd.read_csv("./global_sales_data/market_fact.csv")
'''
=======
df=pd.read_csv("market_fact.csv")

>>>>>>> 7d07155d6f83d155a053ac6b5dc8d1d0981e58f2
sns.distplot(df['Shipping_Cost'])
plt.show()

#subplots 
'''
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
<<<<<<< HEAD
'''
# box plot
'''sns.boxplot(df['Order_Quantity']) # it is default on x-axis
plt.show()
# for y axis
sns.boxplot(y=df['Order_Quantity'])
plt.show()
'''

#sns.jointplot('Sales','Profit',df)
#plt.show() #otuput is heavyily skewed so we aplly condn
'''
df=df[(df.Profit<10000) &(df.Sales<20000)]
sns.jointplot('Sales','Profit',df,kind="hex",color="k")
plt.show() 
'''

   ''' btc = pd.read_csv("Crypto_data/bitcoin_price.csv")
    ether = pd.read_csv("Crypto_data/ethereum_price.csv")
    monero = pd.read_csv("Crypto_data/monero_price.csv")
    neo = pd.read_csv("Crypto_data/neo_price.csv")
    quantum=pd.read_csv("Crypto_data/qtum_price.csv")
    ripple=pd.read_csv("Crypto_data/ripple_price.csv")

read from telcov.ipynb file'''
=======
# box plot
>>>>>>> 7d07155d6f83d155a053ac6b5dc8d1d0981e58f2
