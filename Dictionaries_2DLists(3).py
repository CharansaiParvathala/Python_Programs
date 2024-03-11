print('2D Lists :')
list2D = [[1,2,3],
           [4,5,6],
           [7,8,9],
           ['*',0,'#']]
 
#Printing 2D list items combined togather
print("\nAll 2D list items combined togather")
print(list)

#Printing 2D list items seperated by each list
print("Seperated each list in 2D list")
for keys in list2D:
           print(keys)
          
#Printing each list items individually
print('Seperate every item in the list')
for keys in list2D:
           for key in keys:
           	print(key,end=' ')
           print()




print("\n\n\nDictionary : ")
dictionary = {'CSE':'Programming',
                        'ECE':'Components',
                        'EEE':'Electronics',
                        'Civil':'Construction',
                        'Mech':'Machines'}

print("\nDictionary Items:")
print(dictionary)

cse = dictionary.get('CSE')
print("\nDictionary get method with key CSE : "+cse)

dictionary.update( {'EEE':'Electrical'} )
print('\nEEE key value updated : '+dictionary.get('EEE'))

dictionary.pop('ECE')#removes the specified value
print("\nECE poped from dictionary : "+str(dictionary))

dictionary.popitem()#removes the last value
print("\nPoped letest value : "+str(dictionary))

keys = dictionary.keys()
print('\nGetting Keys from the dictionary ')
print('M1 : Printing all keys togather : \n '+str(keys))
print('M2 : Printing each key individually : ')
for key in keys:
	print(key,end=' ')

values = dictionary.values()
print("\n\nEvery value in dictionary : ")
for value in values: #we can use m1 or m2 for printing
	print(value,end=' ')
	
items = dictionary.items()
print('\n\nPrinting keys & their values : ')
for key,value in items:
	print(key+':'+value)