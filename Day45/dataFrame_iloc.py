import pandas

student_df = pandas.DataFrame({'name':['charan','sai','kiran','varun'],
                              'age':[18,16,19,14],
                              'branch':['cse','cse','ece','eee']})
#Access first row all columns
print(student_df.iloc[0])
#Access first row 2, 3 columns
print(student_df.iloc[0,[1,2]])
#Access 1-2 rows, 2-3 columns
print(student_df.iloc[0:1,1:2])
