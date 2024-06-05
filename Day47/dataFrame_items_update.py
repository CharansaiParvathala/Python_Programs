import pandas

df = pandas.DataFrame({'name':['charan','kiran','sai'],
                       'age':[18,16,15],
                       'marks':[80,24,27]})
print(df)

#Creating new column and assigning value based on condition
df.loc[ df['age'] <= 18, 'adult' ] = True
print(df)

#Creating new column and assigning values
#with help of apply method
df['status'] = df['marks'].apply(lambda m : 'Fail' if m<27 else 'Pass')
print(df)
