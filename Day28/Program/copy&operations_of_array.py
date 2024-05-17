from  numpy import *
a = array([90, 6, 2, 83, 0])

print('Array :', a)
print('Square root :', sqrt(a))
print('Max :', max(a))
print('Sine :',sin(a))
print('Square :', a ** 2)
a.sort() #sort the array actual values
print('Sorted Array :', a)

#Copying an array:
asc = a.view() #1.shallow copy
adc = a.copy() #2.deep copy
a[0] = 200 #changing original array values
print('Original array after change :',a)
print('Shallow Copy :',asc)
print('Deep copy :',adc)