from numpy import *

arr1 = array((1,2,3,4,5))
#default data type of array depends on python predefined type conversion
print(arr1) #int

arr2 = linspace(1,5,5) #default datatype is float
print(arr2)

arr3 = logspace(1,3,3) #default datatype is float
print(arr3)

arr4 = arange(1,3,1)#depends on predefined conversion
print(arr4)

arr5 = zeros(5)#float
print(arr5)#default values 0's

arr6 = ones(5)#float
print(arr6)#default values 1's