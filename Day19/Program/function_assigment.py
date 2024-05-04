p = print #assigning predefined function 

def say(no,msg):
	print("Say Function Called")
	for i in range(no):
		p(msg,i)
		
s = say #assigning user defined function say adress to s variable
print(s)
s(2,"Hello") #using s variable instead of say()