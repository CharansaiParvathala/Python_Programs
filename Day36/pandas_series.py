import pandas as pd

s = pd.Series([1,3,5,8])
print('indx vals')
print(s)
print('Count :',s.count())
print('Mean :',s.mean())
print('Standard Deviation :',s.std())
print('Min :',s.min(),'\nMax :',s.max())
print('\nAll attribtes with describe() :',s.describe())