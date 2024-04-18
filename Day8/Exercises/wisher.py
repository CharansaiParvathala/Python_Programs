import time

def timer(stop, message, start = 0 , remind = 'Begin :'):
	
	print("\n"+remind)
	
	for i in range(start, stop+1):
		time.sleep(1)
		print(i)
				
	print(message)

e = int(input("Enter Ending point : "))
emsg = input("Enter Ending Message : ")
timer(e, emsg) #calling function by ommiting default arguments remind,start


s = int(input("\n\nEnter Starting point : "))
smsg = input("Enter Starting Message : ")
e = int(input("Enter Ending point : "))
emsg = input("Enter Ending Message : ")

timer(e, emsg, s, smsg) #calling functon without ommiting any argument'
