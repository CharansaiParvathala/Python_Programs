from math import e #built in

def outer():
	v = 20 #local
	print('outer function v after changing it : ',v)
	print('built in variable in outer : ',e)
	def inner():
		v = 30#enclosed
		print('inner functon call after assigning : ',v)
	inner()
	print('outer function V after calling inner function : ',v,'\n')
	print('built in variable in inner : ',e)
	
def outer2():
   print('outer function without assigning : ',v)
   def inner2():
   	print('inner functon without assigning : ',v,'\n')
   inner2()
	
	
v = 0#global
print('main function v : ',v)
print('built in variable in main : ',e)
outer()
print('main function v after calling outer : ',v)
print('built in variablein main after calling outer : ',e,'\n')
outer2()


'''
Scope :
	Built-in>Global>Enclosed>Local
	BGEL
Revolution :
	Local>Enclosed>Global>Built-in
	LEGB
'''
