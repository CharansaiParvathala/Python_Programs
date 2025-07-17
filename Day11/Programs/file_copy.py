import shutil as s
import os

filepath = 'file.txt'

copyfilepath = '/storage/emulated/0/Documents/Pydroid3/Python_Programs/copied_with_copyfile.txt'

s.copyfile(filepath,copyfilepath)

if os.path.exists(copyfilepath):
	print("File copied succesfully.")

'''
copyfile : only cpoies file content
copy : copy file content along with directory or path
copy2 : copy file content , path with meta data (data about file or data about data: file created date,file nane etc)
'''