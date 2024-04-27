class P1:
	def p1(self):
		print('1st Parent class method')

class P2:
	def p2(self):
		print('2nd Parent class method')
		
class C(P1,P2):
	def c(self):
		print('Child class method')

c = C() #child class obj creation

c.c()
c.p1()
c.p2()
