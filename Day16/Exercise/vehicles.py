from abc import ABC,abstractmethod

class vehicle(ABC):          #using ABC class to implement Abstract class
	@abstractmethod #using abstractmethode to define a abstract method in abstract class
	def start(self):
		pass
	@abstractmethod
	def stop(self):
		pass
		
class car(vehicle):  #inheriting abstract class
	name = None
	def __init__(self,name):
		self.name = name
		print(self.name,'car is manufactured!')
		
	def start(self): #covert abstract method into concrete methode
		print(self.name,'Started')
		
	def stop(self):  #covert abstract method into concrete methode
		print(self.name,'stoped')

#if we don't covert abstractmethod into concrete it will generates an error'

bmw = car("BMW")
bmw.start()
bmw.stop()
