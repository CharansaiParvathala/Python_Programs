import time #importing time module to use sleep function
#we will discuss about modules indetailed later
#we use f in python to ptint variable values more easily like guven below
#print(f'{variable:formate}')
timer = int(input("Enter Time In Secods : "))

for i in range(timer,0,-1):
	sec = i%60
	min = int(i/60)%60
	hr = int(i/3600)
	
	time.sleep(1)  #using sleep methodvit will pause exicution for 1 sec
	print(f"{hr:02}:{min:02}:{sec:02}")
	
print("Time Out!")