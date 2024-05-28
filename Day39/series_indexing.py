import pandas as pd

sr = pd.Series([2,6,19,60],index=['a','b','c','d'])
#single element accesing
print('Accesing using default index :',sr.iloc[1],end=', ')
print('Accesing using user index :',sr.loc['b'])
#Range accesing
print(f'Range accesing:\n{sr.loc['a':'c']}')
#Filterig
print(f'below 10 numbers:\n{sr[sr < 10]}')