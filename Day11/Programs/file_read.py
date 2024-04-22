with open('/storage/emulated/0/Documents/Pydroid3/Python_Programs/file.txt') as file:
	print('File is exits and it store these info :\n')
	print('**\n'+file.read()+'\n**')
	
"""
With Open() Operation automatically closes the file
	if didn't use with open() we need to close at end of the file 
	default open mode is read -> open('file.txt','r') if we want to change we can change it
"""