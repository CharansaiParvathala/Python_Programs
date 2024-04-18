#Functons, return, Normal arguments

def function1(): #with no arguments
	print("Function 1 Called!")
	
def function2(v):#function with integer argument
	print(f"Function 2 Called with {v} argument!")
	
def function3(name):#functon with string argument&retrun
	print(f"Function Called with {name} argument return Value :")
	return name.upper() #string return

#Function Calling
function1()

function2(10)

print(function3("charan"))
