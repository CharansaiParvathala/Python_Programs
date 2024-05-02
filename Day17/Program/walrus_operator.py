
"""
Example program without := operator:
	
	products = []
	while  True:
		food = input('Enter Your Fav Product: ')
		if food = 'e':
			break
		else:
			foods.append(food)
"""

#Same Program using Walrus := Operator
foods = []
while food := input('Enter Your Fav Product: ') != 'e' :
	foods.append(food)