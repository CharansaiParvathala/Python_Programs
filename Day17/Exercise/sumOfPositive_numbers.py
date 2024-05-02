def psum():
    total = 0
    while (number := int(input("Enter a number (negative to stop): "))) > 0:
        total += number
    return total

result = psum()
print("Sum of positive numbers entered:", result)
