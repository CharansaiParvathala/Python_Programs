import shutil as s

filepath = 'file.txt'

copyfilepath = '/storage/emulated/0/Documents/Pydroid3/Python_Programs/copied_with_copyfile.txt'

s.copyfile(filepath,copyfilepath)

'''
copyfile : only cpoies file content
copy : copy file contet along with directory or path
copy2 : copy file content , path with meta data (data qbout file : file created date,file nane etc)
'''