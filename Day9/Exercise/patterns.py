def  rigth_half_pyramid():
	print("\nRigth Half Pyramid :")
	for i in range(x):
		print(x*" "+i*"*")

def left_half_pyramid():
	print("\nLeft Half Pyramid")
	for i in range(x):
		print(x*" "+(x-i)*" "+i*"*")

def full_pyramid():
	print("\nFull Pyramid")	
	for i in range(1,x):
		print(x*" "+int(x-i)*" ",end ="")
		j=1
		while j != i:
			print("*"+" ",end="")
			j+= 1
		print("*")

def rambus():
	print("\nRambus :")
	for i in range(x):
		print(x*" "+i*" "+x*"*")
	
def hallow_square():
	print("\nHallow Square :")
	for i in range(x):
		print(x*" ",end="")
		if i == 0 or i == x-1:
			print(x*"*")
		else:
			print("*"+(x-2)*" "+"*")
			
while True:
	print("\n1.Rigth Half Pyramid\n2.Left Half Pyramid\n3.Full Pyramid\n4.Rambus\n5.Hallow Square\n6.Exit\n")
	op = int(input("Enter Your Choice : "))
	if op<6:
		x = int(input("Enter size : "))
	if op == 1:
		rigth_half_pyramid()
	elif op == 2:
		left_half_pyramid()
	elif op == 3:
		full_pyramid()
	elif op == 4:
		rambus()
	elif op == 5:
		hallow_square()
	elif op == 6:
		print("thank you for visiting")
		break
	else:
		print("Please enter a valid choice")

