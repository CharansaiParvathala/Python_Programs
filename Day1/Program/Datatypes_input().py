# Storing different types of data in variables
integer_val = 42 #int
float_val = 3.14 #float
complex_val = 2 + 3j #complex
str_val = "Hello, Python!" #str
bool_val = True #bool

# Printing stored values along with data types
print("Stored Integer:", integer_val, "| Type:", type(integer_val))
print("Stored Float:", float_val, "| Type:", type(float_val))
print("Stored Complex:", complex_val, "| Type:", type(complex_val))
print("Stored String:", str_val, "| Type:", type(str_val))
print("Stored Boolean:", bool_val, "| Type:", type(bool_val))

# Example of input and type casting
user_input = input("Enter an integer: ")  # Accept integer input from user
user_int = int(user_input)  # Convert input to integer

print("User Input (Integer):", user_int, "| Type:", type(user_int))

# Multiple assignments
x=y=z= 100 #Multiple assignments for sane value
a, b, c = 10, 20, 30  # Multiple assignments for different values

print("Multiple Assignment Values - x:", x,", y:",y,", z:",z)
print("Multiple Assignment Values - a:", a,", b:",b,", c:",c)