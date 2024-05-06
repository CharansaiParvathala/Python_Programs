def combine(s1):
	x = lambda s2:s1+s2
	return x

greet = input("Enter your greets :")+" "

g = combine(greet)

while (name := input("Enter name (e for exit):")) != 'e':
	print(g(name),end="\n\n")