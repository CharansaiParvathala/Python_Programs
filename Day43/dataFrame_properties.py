import pandas as pd

df = pd.DataFrame({'name':['charan','sai'],
'age':[18,15],
'sec':['B','A']})
print(df.shape)
print(df.columns)
print(df.dtypes)
#Returns mathematical calculations of df values
print(df.describe())
