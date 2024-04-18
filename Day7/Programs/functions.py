#functions, return, normal arguments, Parameters

def function1(): #with no parameters
	print("Function 1 Called!")
	
def function2(v):#function with integer parameter
	print(f"Function 2 Called with {v} parameter!")
	
def function3(name):#functon with string parameter &retrun
	print(f"Function Called with {name} parameter and return Value :")
	return name.upper() #string return

#Function Calling
function1()

function2(10) #integer argument

print(function3("charan")) #string argument
