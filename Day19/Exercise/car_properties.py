status = "stopped"
def start():
	global status
	status = "started"
	print(f"Car  {status}.")
	
def stop():
	global status
	status = "stopped"
	print(f"Car {status}.")
	
def rise():
	if status == "started":
		print("Car speed rised.")
	else:
		print("Please start the car.")

fl = [start,rise,stop,rise]  #Assigning function to the list

for f in fl:
	f()  #using  list to call function
	