from numpy import *
n = int(input('Enter size of the array:'))
arr = zeros(n,int)
for i in range(n):
    arr[i] = int(input(f"Enter Element {i+1}:"))

key = int(input('Enter kay to search:'))
i=0
while i<n:
    if arr[i]==key:
        print(f'Element found at index no:{i}')
        break
    i += 1
else:
    print('Element not found')

