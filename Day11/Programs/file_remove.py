import os
path = '/storage/emulated/0/Documents/Pydroid3/Python_Programs/copied_with_copyfile.txt'
try:
	os.remove(path)
except FileNotFoundError:
	print('File not exists ')
except PermissionError:
	print('Permision denied by system')
else:
	print(path,'\n*is deleted*')
	
'''
import os

os.remove()  Remove certai  file
os.rmdir()  Remove empty directory

import shutil

shutil.rmtree() Remove directory including files present in it
'''