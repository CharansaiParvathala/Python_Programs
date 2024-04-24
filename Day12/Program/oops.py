#Oops in python

class Mobile:
	
	def __init__(self,brand,model,ram,price):
		self.brand = brand    #instace variable >variable which inside the constructor or methode
		self.model = model
		self.ram = ram
		self.price = price
		self.state = 'Mobile status : locked'
		
	def status(self):
		print(self.model,self.state)
		
	def unlock(self):
		self.state = 'Mobile status : Unlocked'
		
	def lock(self):
		self.state = 'Mobile status : locked'

#Using Mobile class methods & attributes with help of object

mobile1 = Mobile('redmi','RMN10','6GB',15999)
mobile2 = Mobile('moto' ,'ME60','8GB',32999)
print(mobile1.brand)
print(mobile1.model)
print(mobile1.ram)
print(mobile1.price)

mobile1.status()

mobile1.unlock()
mobile1.status()

mobile1.lock()
mobile1.status()


mobile2 = Mobile('moto' ,'ME60','8GB',32999)
print('\n'+mobile2.brand)
print(mobile2.model)
print(mobile2.ram)
print(mobile2.price)

mobile2.status()

mobile2.unlock()
mobile2.status()

print()
mobile1.status()
mobile2.status()
