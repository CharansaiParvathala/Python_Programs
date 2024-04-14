# Example of a for loop iterating over a string
print("Example of a for loop iterating over a string:")
message = "Hello"
for char in message:
    print(f"Character: {char}")
    if char == "l":
        print("Encountered 'l' - breaking the loop")
        break  # Exit the loop when 'l' is encountered
else:
    print("Loop completed without encountering a break")

print("\n")

# Example of a while loop counting from 1 to 5
print("Example of a while loop:")
count = 1
while count <= 5:
    if count == 3:
        print("Skipping count 3")
        count += 1
        continue  # Skip to the next iteration when count is 3
    print(f"Current count: {count}")
    count += 1
    if count == 5:
        print("Reached count 5 - breaking the loop")
        break  # Exit the loop when count reaches 5
else:
    print("While loop completed")

print("\n")

# Example of a for loop with range() function
print("Example of a for loop using range():")
for i in range(1, 6):  # Iterate over numbers 1 to 5
    if i % 2 == 0:
        print(f"Even number: {i}")
    else:
        print(f"Odd number: {i}")

print("\n")

# Example of a for loop iterating over a custom iterable (string)
print("Example of a for loop iterating over a custom iterable (string):")
word = "Python"
for ch in word:
    if ch == 't':
        continue  # Skip printing 't', and continue with the next iteration
    print(ch)

print("\n")

print("Loop examples complete!")
