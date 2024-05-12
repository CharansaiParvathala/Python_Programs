def square(l):
    return [i*i if type(i) in [int,float] else None for i in l]

l = [3,9.4,'hi',0.5,7,]
s = square(l)

for i,i2 in zip(l,s):
    print(f'Square of {i} = {i2}')