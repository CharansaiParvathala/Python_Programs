l = ['madara','killua','zoro','senku','goku'] #storing Names
f = lambda name : 'Hi '+name #lambda expression that concates hi to the name
greet = map(f,l)  #map() it takes two arguments (functin, iterable)
for i in greet:
    print(i)