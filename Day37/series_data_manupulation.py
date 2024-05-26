import pandas as pd
sr = pd.Series([3,1,2])
print(f'Series :\n{sr}')
f = lambda e:e**2
#map only works with series not with data frame
sqr_sr = sr.map(f)
#apply works for series as well as data frame
sqr_sr = sr.apply(f)
print(f'squares of series :\n{sqr_sr}')
#sorting series values
print(f'sorted series:\n{sr.sort_values()}')
#below way don't effect original series
#it returns new series
d_sr = sr.drop(0)
#below way effects original series
#modifies values in actual series
sr.drop(0,inplace=True)
#we can also use these method with sort.
print(f'drop values in series:\n{sr}')