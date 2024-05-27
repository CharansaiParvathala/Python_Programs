import numpy as np
import pandas as pd

sr = pd.Series([np.nan])
print(f'Series :\n{sr}')
#Checks the every element in series
#wether it is null(NAN,None)
print(sr.isnull())
#checks value is not null
print(sr.notnull())
#Fill all null values with specified value
print(sr.fillna(3))
#Drops all null values
print(sr.dropna())