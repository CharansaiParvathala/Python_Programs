# Sample data dictionary containing student details
data = {
    '5D1': {
        'details': [['charan', 'CSE', 'Male'], ['momidi', '18', 'Male']]
    },
    '5B0': {
        'details': [['hemanth', 'CSE', '2nd year'], ['atmakur', '19', 'Male']]
    },
    '499': {
        'details': [['mass', 'ECE', '2nd year'], ['varagali', '21', 'Male']]
    }
}

# Get all keys (student IDs) from the data dictionary
keys = data.keys()
for key in keys:
    print(key)  # Print all available student IDs

# Prompt user to choose a student ID
student_id = input("Choose Student ID:").upper()

# Check if the chosen student ID exists in the data dictionary
if student_id in data:
    # Retrieve student details for the chosen ID
    student_details = data[student_id]['details']
    if student_details:
        # Extract specific details from the nested list
        name, branch, gender = student_details[0]
        place, age, gender = student_details[1]
        # Display the retrieved details
        print("Student ID:", student_id)
        print("Name:", name)
        print("Branch:", branch)
        print("Gender:", gender)
        print("Place:", place)
        print("Age:", age)
else:
    print("Student not found")  # Print message if student ID is not found
