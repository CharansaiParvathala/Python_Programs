import pandas

df = pandas.DataFrame({'name':['charan','kiran','sai'],
                       'age':[18,16,15],
                       'sec':['a','b','a'],
                       'marks':[80,24,79],
                       'fees':[4000,14000,3000]})
#Giving Name to Indexes
df.index.names = ['ID']
print(df,'\n')
#Creating new column by combining two existing columns
df['name & fee'] = df['name']+'('+df['fees'].astype(str)+')'
print(df)
#Changing Column Name
df.rename(columns={'fees':'pending'},inplace=True)
print(df)
#Assigning multiple columns to data frame
df = df.assign(adult = lambda x: x['age']>=18,
               Pass = lambda x: x['marks']>=27)
print(df)