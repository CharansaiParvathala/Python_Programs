vehicles = ["car","bike","cycle"] #List [list of items]
#changable & contains duplicate values

#help(vehicles)
#print(dir(vehicles))  To known about list related functions

print("List : "+str(vehicles))

l = len(vehicles)
print("\nLength of the list : "+str(l))

vehicles.append("bus")
print("Appended : "+str(vehicles))

vehicles[3] = "bike"
print("Changed : "+str(vehicles))

vehicles.insert(0,"boat")
print("inserted at 0 : "+str(vehicles))

vehicles.remove("boat")
print("Removed boat : "+str(vehicles))

print("bike count in list : "+str(vehicles.count("bike")))

print("Index of the bike : "+str(vehicles.index("bike",2)))
#                          refers to the second bike in the list ^

print("there is cycle in the list : "+str("cycle" in vehicles))

vehicles.sort()
print("Sorted list : "+str(vehicles))

vehicles.reverse()
print("Reversed list : "+str(vehicles))

vehicles.clear()
print("Clear all items in list : "+str(vehicles))



names = {"charan","kiran","tharun"} #sets {}
#UnOrdered & immutable but we can add&remove items. contains duplicates
print("\n\n\nSet : "+str(names))

names.add("varun")
print("\nAdd to set : "+str(names))

names.remove("tharun")
print("remove from set : "+str(names))

names.pop()
print("pop from set : "+str(names))

names.add("varun")
print("try to add duplicate item : "+str(names))

#names[0]="charan"  generates error because set is immutable



cars = ("volvo","tata") #tuples
#Ordered & unchangable. contains duplicates. Fster then lists

print("\n\n\nTuple : "+str(cars)) 

count = cars.count("volvo")
print("volvo couts : "+str(count))

#cars[0] = "bmw" generates error because tuples are unchagable

#cars.add("bmw") not possible because tuples are unchagable