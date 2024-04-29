class C:
	def m1(self):
		print('m1')
		return self
		
	def m2(self):
		print('m2')
		return self
		
	def m3(self):
		print('m3')
		return self
	def m4(self):
		print('m4')

c = C()

c.m1().m2().m3().m4()  #methode chaining
