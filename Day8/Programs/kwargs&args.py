def args(*elements): #*args can receive multiple values with same name
#*args are nothing but a tuple type
	print("args data type :",type(elements))
	for element in elements:
		print(element,end=" ")
	print()
	
def kwargs(**data): #**kwargs can receive multiple values with different names
#*args are nothing but a dictinary type
	print("\nKwargs Data type :",type(data))
	for key,item in data.items():
		print(key + ':' + str(item))


args(1,2,3,4,5)
kwargs(name='Charan',
               age=18,
               branch='cse')
