vehicles = ["car","bike","cycle"] #List [list of items]
#changable & contains duplicate values

#help(vehicles) To known about list related functions along with explaination
#print(dir(vehicles))  To known about list related functions

print("List of items : ",vehicles)

l = len(vehicles)
print("Length of the list : ",l)

vehicles.append("bus")
print("\nAppended : ",vehicles)

vehicles[3] = "bike"
print("Changed : ",vehicles)

vehicles.insert(0,"boat")
print("inserted at 0 : ",vehicles)

vehicles.remove("boat")
print("Removed boat : ",vehicles)

print("bike count in list : ",vehicles.count("bike"))

print("Index of the bike : ",vehicles.index("bike",2))
#                          refers to the second bike in the list ^

print("there is cycle in the list : ",("cycle" in vehicles))

vehicles.sort()
print("Sorted list : ",vehicles)

vehicles.reverse()
print("Reversed list : ",vehicles)

vehicles.clear()
print("Clear all items in list : ",vehicles)
