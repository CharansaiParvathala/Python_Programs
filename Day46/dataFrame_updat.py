import pandas

df = pandas.DataFrame({'name':['charan','kiran','sai'],
                       'age':[18,16,15],
                       'sec':['a','b','a']})
print(df)
drop_df = df.drop(labels='sec',axis=1)
#can also make change directly in df with inplace=True
print(f'Deleted DataFrame:\n{drop_df}')
update_df = df.at[1,'age'] = 19
print(f'Updated df :\n{update_df}')
df['new_column'] = None
print(df)