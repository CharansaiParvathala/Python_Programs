data = {
    '5D1': {
        'details': [['charan', 'CSE', '2nd year'], ['momidi', '18', 'Male']]
    },
    '5B0': {
        'details': [['hemanth', 'CSE', '2nd year'], ['atmakur', '19', 'Male']]
    },
    '499': {
        'details': [['mass', 'ECE', '2nd year'], ['varagali', '21', 'Male']]
    }
}
keys = data.keys()
for key in keys:
	print(key)

student_id = input("Choose Student ID:").upper()

if student_id in data:
    print("\n*****STUDENT INFORMATION****")
    student_details = data[student_id]['details']
    if student_details:
        name, branch, year = student_details[0]
        place, age, gender = student_details[1]
        print("Student ID:", student_id)
        print("Name:", name)
        print("Branch:", branch)
        print("Year:", year)
        print("Place:", place)
        print("Age:",age)
        print("Gender:", gender)
else:
    print("Student not found")
