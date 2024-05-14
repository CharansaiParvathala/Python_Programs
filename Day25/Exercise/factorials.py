def factorials(n):
    i = 1
    while(i<=n):
        f=j = 1
        while(j<=i):
            f = f*j
            j += 1
        i += 1
        yield f
n = int(input('Enter factorials range:'))
f = factorials(n)
for i in range(n):
    print(next(f))