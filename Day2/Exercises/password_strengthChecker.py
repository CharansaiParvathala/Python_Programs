s = input("Enter your Password : ")
l = 0
c1=c2=False

#Logic Build only using conditinal statements
if len(s)>5:
	l += 1
else:
	l -= 1
if not(s.upper==s or s.lower()==s):
	l +=1
else:
	l -=1
if not(s.isalnum()):
	l +=2
elif not(s.isdigit() or s.isalpha()):
	l  +=1
else:
	l -=1

if l<1:
		print("Your Password is Very Weak")
elif l<2: 
		print("Your Password is Weak")
elif l<4:
		print("Your Password is Strong")
else:
		print("Your Password is very Strong")
		
