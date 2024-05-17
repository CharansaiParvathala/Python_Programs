from numpy import *
print('press enter for stop and continue for space')
a1 = array(input('Enter array1 elements:').split())
a2 = array(input('Enter array2 elements:').split())

print(f'\nBefore swapping :\nArray1:{a1}\nArray2{a2}')
#Array swapping with temperary variable
temp = a1.copy()
a1 = a2
a2 = temp
print(f'After swappping :\nArray1:{a1}\nArray2:{a2}')