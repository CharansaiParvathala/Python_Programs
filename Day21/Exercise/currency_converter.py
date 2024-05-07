items = [
    ('Pen',10.0),
    ('notes',60.0),
    ('mobile',15000.0),
    ('laptop',50000.0)
]

usd = lambda i : (i[0],round(i[1]/83.51))
pk = lambda i : (i[0],round(i[1]/0.3))
jpn = lambda i : (i[0],round(i[1]/0.54))
items_dollers = map(usd, items)
items_pkr = map(pk, items)
items_yen = map(jpn, items)

for i1,i2,i3 in zip(items_dollers,items_pkr,items_yen):
#we are using zip function it combines multiple iterables
#we discuss about it indetailed later days
    print(i1[0],'=',i1[1],'dollers')
    print(i3[0], '=', i3[1],'pkr')
    print(i3[0], '=', i3[1],'yen')
