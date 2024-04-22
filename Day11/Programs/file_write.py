text = "Hi\nThis is a File\nWritten in python program"
textappend="\nThis message is appended"
path = '/storage/emulated/0/Documents/Pydroid3/Python_Programs/file.txt'
with open(path,'w') as file:
	file.write(text)
with open(path,'a')as file:
	file.write(textappend)
	
'''
a = append
w = write
'''