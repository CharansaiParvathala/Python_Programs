class Vehicle:
	company = None #class variable
	name = None
	model = None
class  Car(Vehicle):
	def __init__(self,doors,ac):
		self.doors = doors #instace variable
		self.ac = ac
class Bike(Vehicle):
	def __init__(self,type):
		self.type = type #instace variable

b1=Bike('2 Wheels Motor cycle')
b1.company = 'Yamaha'
b1.name = 'Yamaha master 250'
b1.model = 'YMM250C'

b2=Bike('3 Wheels scooter')
b2.company = 'Pulsur'
b2.name = 'Pulsur S2 220'
b2.model = 'PS220C'


c1=Car(2,False)
c1.company = 'Suzuki'
c1.name = 'Susuki super 12'
c1.model = 'SS12'

print('Bike :',b1.name)
print(b1.company)
print(b1.model)
print(b1.type)

print('\nBike :'+b2.name)
print(b2.company)
print(b2.model)
print(b2.type)

b1.company = 'KTM'  #class varible change with constructor or methode does nor effect the Class.variable value
b2.company = 'Duke'

print('\n'+b1.company)
print(b2.company)
print(Bike.company)

Bike.company = 'Nothing' #only effects class variable when it is changed with class object
print('\n'+Bike.company)