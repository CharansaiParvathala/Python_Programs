import os

source = '/storage/emulated/0/Documents/Pydroid3/Python_Programs/source.txt'
destination = '/storage/emulated/0/Documents/Pydroid3/source.txt'
try:
	if os.path.exists(destination):
		print('That file already exists in the destination path')
	else:
		os.replace(source,destination)
		print('File moved to ',destination)
except FileNotFoundError:
		print('Source File not exists')
		