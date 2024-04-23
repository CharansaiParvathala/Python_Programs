import os
import  shutil as s
files = []
def f_write():
    global files
    name = input("\nEnter file name :")
    data = input("Enter data to store in file :")
    if os.path.exists(name):
        with open(name, 'a') as file:
            file.write(data)
    else:
        files.append(name)
        with open(name, 'w') as file:
            file.write(data)
    print("file writing is successful")
    
def  f_check():
	name = input("\nEnter file name :")
	if os.path.exists(name):
		print("Its Exits")
		if os.path.isfile(name):
			print('It is a file')
		elif os.path.isdir(name):
			print('It is a directory')
	else:
		print('It does`t Exists')

def f_read():
    name = input("\nEnter file name :")
    try:
        with open(name, 'r') as file:
        	print(file.read())
    except FileNotFoundError:
       print("File not found !")
       
def f_move():
	source = input("\nEnter source file to move :")
	destination = input("Enter destination path with file name :")
	try:
		os.replace(source,destination)
	except FileNotFoundError:
		print("File not found !")
	except FileExistsError:
		print("File already exists in destination !")
	except Exception:
		print("Unexpected error occured !")
	else:
		print("Your file moved to",destination)
def f_copy():
		name = input("Enter file name :")
		copyfilepath = input("Enter file copy path :")
		try:
			s.copyfile(name,copyfilepath)
			print(name,"File copied succefully.")
		except FileNotFoundError:
			print("File not found !")
		except FileExistsError:
			print("File already exists in that path !")
		except Exception:
			print("Unexpected error occured !")
		
def f_remove():
	name = input("\nEnter file name :")
	try:
		os.remove(name)
		print(name,"file is deleted.")
	except FileNotFoundError:
		print("File is already deleted !")
	except Exception:
		print("Unxpected error accured !")
		
def f_view():
	global files
	print()
	for file in files:
		print(file)
	

while True:
    print('\n1.create file','2.check file details','3.read file','4.move file','5.copy file','6.remove file','7.view recently created files','8.exit',sep="\n")
    op = int(input("Enter your choice :"))
    if op == 1:
        f_write()
    elif op == 2:
    	f_check()
    elif op == 3:
        f_read()
    elif op == 4:
    	f_move()
    elif op == 5:
    	f_copy()
    elif op == 6:
        f_remove()
    elif op == 7:
    	f_view()
    elif op == 8:
    	break
    else:
        print("Enter valid option!")
  
