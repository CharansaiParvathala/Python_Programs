names = {"charan","kiran","tharun"} #sets {}
#UnOrdered & immutable but we can add&remove items. contains duplicates
print("Set of items : ",names)

names.add("varun")
print("\nAdd to set : ",names)

names.remove("tharun")
print("remove from set : ",names)

names.pop()
print("pop from set : ",names)

names.add("varun")
print("try to add duplicate item : ",names)

#names[0]="charan"  generates error because set is immutable

cars = ("volvo","tata")
#Ordered & unchangable. contains duplicates. Fster then lists

print("\n\nTuples : ",cars) #tuples()

count = cars.count("volvo")
print("volvo couts : ",count)

#cars[0] = "bmw" generates error because tuples are unchagable

#cars.add("bmw") not possible because tuples are unchagable
