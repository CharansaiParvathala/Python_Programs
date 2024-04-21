''' 
a/b = 10/0 - ZeroDivisionError
a/c = 10/vv - TypeError
'''
   
a = 10
b = 0
c = "String"
try:
	res = a/b #Code that generates Exception
	
except ZeroDivisionError as e:
	print('you cant divide any number with zero 0')
	print(e)
  
except TypeError as e:
	print('Please anter Number Type')
	print(e)
  
except Exception as e:
	print('Unknown Exception')
	print(e)
	
else:
	print("We didn't get any exceptions res : ",res)
	
finally:
	print('programm Excution completed!')
