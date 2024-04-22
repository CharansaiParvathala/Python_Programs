import os

p = "file.txt"
if os.path.exists(p):
	print("Its Exits")
	if os.path.isfile(p):
		print('It is a file')
	elif os.path.isdir(p):
		print('It is a directory')
else:
	print('It does`t Exists')