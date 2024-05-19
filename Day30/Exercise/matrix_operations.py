from numpy import *
n1,n2 = (int(input('Enter number of rows:'))
         ,int(input('Enter number of colunms:')))
a = zeros(n1 * n2, int)
b = zeros(n1 * n2, int)

for i in range((n1*n2)):
    a[i] = int(input(f'Enter element {i + 1} for matrix a:'))
    b[i] = int(input(f'Enter element {i + 1} for matrix b:'))
a, b = a.reshape(n1, n2), b.reshape(n1, n2)

print('\nMtrix Multiplication :\n',a*b)
print('Matrix Addtion :\n',a+b)
print('Matrix Subtraction :\n',a-b)