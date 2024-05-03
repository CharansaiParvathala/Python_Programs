import functools as f #To use reduce function

#lambda
addition = lambda *numbers : sum(numbers)
print("Sum of multiple numbers using lambda expression : ",addition(2,3,4,6,6,5,8,10,6,9,10,1,30))


#Reduce
'''
to use reduce function we need to import functools module:
	import functools
syntax:
	reduce(function, list)
'''
chars = ['c','h','a','r','a','n']
print("\nchars list before reducing :",chars)
combine = lambda x,y:x+y
word = f.reduce(combine,chars)
print("After reducing :",word)
