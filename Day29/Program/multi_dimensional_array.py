from numpy import *

arr1 = array([[1,2,3],
         [4,5,6],
         [7,8,9]])
print('1.array :\n',arr1)
print('2.dimensions :',arr1.ndim)
print('3.shape :',arr1.shape)
print('4.size :',arr1.size)

arr2 = arr1.flatten()
print('flatten array :',arr2)

arr3 = arr2.reshape(3,3)
print('reshaped array :\n',arr3)