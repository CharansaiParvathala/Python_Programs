from numpy import *
n1,n2 = (int(input('Enter number of rows:'))
         ,int(input('Enter number of colunms:')))
arr = zeros(n1*n2,int)
for i in range(n1*n2):
    arr[i] = int(input(f'Enter element {i}:'))
arr = arr.reshape(n1,n2)
print('\nArray :')
for a in arr:
    print(a)