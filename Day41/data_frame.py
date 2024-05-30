import pandas as pd
#Creating Data Frame
student = pd.DataFrame({'ID':['5D1','5X1','4Y1'],
                        'NAME':['Charan','Kiran','Tharun'],
                        'BRANCH':['CSE','CSE','ECE']})
print('Student DataFrame:',student,sep='\n')
fees = pd.DataFrame({'ID':['5D1','5X1','4Y1'],
                     'FEE':[20000,25000,15000]})
print('Fees DataFrame:',fees,sep='\n')
merged_df =pd.merge(student, fees, on='ID')
#Meging Two data frames on ID
print('Merged DataFrame:',merged_df,sep='\n')
