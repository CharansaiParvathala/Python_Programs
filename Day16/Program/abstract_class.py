from abc import ABC,abstractmethod

class Abstract(ABC):
	
	@abstractmethod
	def abstract_method1(self):
		pass
		
	@abstractmethod
	def abstract_method2(self):
		pass
		
class Implement(Abstract):
	def abstract_method1(self):
		print("abstract_method1 coverted into concrete method.")
		
	def abstract_method2(self):
		print("abstract_method2 coverted into concrete method.")
		
abc = Implement()
abc.abstract_method1()
abc.abstract_method2()