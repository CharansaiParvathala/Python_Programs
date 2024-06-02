import pandas as pd

student_df = pd.DataFrame({'name':['charan','sai','kiran','varun'],
						'age':[18,16,19,14],
						'branch':['cse','cse','ece','eee']})
print(student_df.head(5))
#returns specified no of rows
print(student_df.loc[:,'name'])
print(student_df.loc[0:2,['name','age']])
print(student_df.loc[student_df['age']>17,['name','branch']])
