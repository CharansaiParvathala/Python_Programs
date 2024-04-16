items = {"Items"}
prices = {0}
total = 0
while True:
	item = input("Enter Product Name (e for exit): ")
	if  item.lower() == "e":
		break
	else:
	    items.add(item)
	    price = int(input("Enter Price : "))
	    prices.add(price)
	    
print("\n*******YOUR CART********")

for item in items:
	print(item, end=",")
	
for price in prices:
	total = total+price
	
print(f"\nTotal Price is {total}")
