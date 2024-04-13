#String Methods in python

s = "Charan Sai"

print("length :",len(s)) #returns length

print("find a :",s.find('a')) #checks a string exists or not in reverse order

print("find a in reverse formate :",s.rfind('a')) #checks a string exists or not in reverse order

print("Capitalized String :",s.capitalize())#capitalize the string

print("Upper case String :",s.upper())#change into upper case

print("Lower case string :",s.lower())#change into lower case

print("Count of 'a' :",s.count('a'))#counts a particular string

print("It is a Number :",s.isdigit()) #check a string is number or not

print("It is an Alphabet :",s.isalpha())#check a string is alphabet or not

print("Replaced String :",s.replace('a','@'))  #replace a string with other string

ss = s.split(' ') #separate a string with particular character or string

print("Substring 1 :",ss[0],", Substring 2 :",ss[1])

#To get all methods related to string we use help function 
#help(str)

#*****String Slicing*****

#string[start : end : step]

print("String from index 0 to end :",s[:])

print("String from index 7 to end :",s[7:])

print("String with two steps :",s[::2])

print("String Reverse with negative index :",s[::-1])
