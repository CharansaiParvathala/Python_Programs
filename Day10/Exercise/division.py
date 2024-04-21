import exception

try:
    n1 = exception.type_exception()
    n2 = exception.type_exception()
    
    try:
        result = n1 / n2
    except ZeroDivisionError:
        n2 = exception.zero_division()
        result = n1 / n2

    print(f"{n1} / {n2} = {result}")
    print("Program Execution completed!")

except Exception as e:
    print("An error occurred:", e)
