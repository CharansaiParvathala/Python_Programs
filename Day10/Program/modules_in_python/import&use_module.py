import module
#import module program using import key word

module.function1() #function1 called with module

print("answer :", module.function2(3))#function2 called with module

#we can also access the functions in module without mentioning module
#by importing all functions from module using * like this
"""
from module import *
function1
function2(3)
#like this we can use functions directly by importing all functions
#from module with from keyword
"""
