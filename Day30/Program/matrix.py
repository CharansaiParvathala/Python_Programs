from numpy import *

m = matrix('10,2,3;4,0,6;7,8,99')
print('matrix :\n',m)

print('1.Diagonal matrix :',m.diagonal())
print('2.A1 Matrix :',m.getA1())
print('3.Horizontal Matrix :\n',m.getH())
print('Max :',m.argmax())
print('Min :',m.argmin())