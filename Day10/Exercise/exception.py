def zero_division():
    print("Division by zero is not possible!")
    while True:
        try:
            n = int(input("Enter another number to perform division: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if n == 0:
            print("Cannot divide by zero. Please enter a non-zero divisor.")
        else:
            return n

def type_exception():
    while True:
        try:
            n = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        else:
            return n
          
