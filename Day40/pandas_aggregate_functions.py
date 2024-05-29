import pandas

sr = pandas.Series([7,3,5])
sum = sr.sum()
csum = sr.cumsum()
cmin = sr.cummin()
agr = sr.aggregate(('sum','mean','std'))
print(f'Sum:{sum}'
      f'cumsum:\n{csum}'
      f'cummin:\n{cmin}'
      f'Agregate methods:\n{agr}')