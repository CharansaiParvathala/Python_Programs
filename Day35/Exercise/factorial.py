def fact(n):
    if n==1:
        return n
    elif n<0:
        return None
    else:
        return fact(n-1)*n
f = fact(int(input('Enter number:')))
print('Factorial :',f)