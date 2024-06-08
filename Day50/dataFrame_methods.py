import pandas

df = pandas.DataFrame({'name':['charan','kiran','sai'],
                       'sec':['a','b','a'],
                       'fees':[4000,14000,None]})
#setting max cols, rows to display
pandas.set_option('display.max_rows',2)
pandas.set_option('display.max_columns',2)
print(df,'\n')
#resetting display options
pandas.reset_option('display')

group = df.groupby('sec')
for g,i in group:
    print('Group :',g)
    print(i)

print(df.count())
print(df.value_counts('sec'))
print('Succesfully completed my 50 Days PythonChallenge')
