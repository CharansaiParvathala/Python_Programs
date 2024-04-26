class animal:
	name = None
	
	def __init__(self,name):
		self.name = name
		
	def eat(self):
		print(self.name,'is eating')
	
	def sleep(self):
		print(self.name,'sleeps')
		
class dog(animal):
	def walk(self):
		print(self.name,'Walkimg')
		
	def bark(self):
		print(self.name,'barks')
		
tom = dog('Tommy')

tom.eat()
tom.bark()
tom.walk()

pup = dog('Puppy')
pup.eat()
pup.bark()

tom.sleep()
pup.sleep()