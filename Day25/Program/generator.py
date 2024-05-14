def generator():
    yield 'Program is loading...'
    yield 'loaded succefully.'
    yield 'Program Over!'

x = generator()

print(next(x),end=' '),input()
print(next(x),end=' '),input()
print(next(x))