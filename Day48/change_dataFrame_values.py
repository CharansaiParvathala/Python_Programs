import pandas

df = pandas.DataFrame({'name':['charan','kiran','sai'],
                       'age':[18,16,15],
                       'sec':['a','b','a']})
print(df)

mapped_df = df['sec'].map({'a':'b'})
print(mapped_df)

replaced_df = df['sec'].replace('a','b')
print(replaced_df)