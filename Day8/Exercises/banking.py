#We are using global keyword in this program which refers the global scope variable
#We discuss about variable scope later in this challenge
#we use end argument in print function which is used to change end value the default value of end is "\n"


# Global variable for balance
balance = 0

def withdraw(*amount):
    global balance
    total = sum(amount) 
    if balance < total:
        print("Insufficient balance!")
    else:
        print("Notes: ", end="")
        for note in amount:
            print(f"{note}rs", end=" ")
        balance -= total
        print(f"\nTotal amount {total}rs withdrawal successful")

def deposit(amount):
    global balance
    balance += amount
    print(f"\nDeposited {amount}rs into account.")

def create(**updates):
    print("\nAccount Created with details:")
    for key, item in updates.items():
        print(f"{key}: {item}")

def check_balance():
	print(f"\nYour Bank Balance is {balance}rs")

name = input("Enter your name: ")
pan_no = input("Enter your PAN card number: ")
number = int(input("Enter your number: "))
age = int(input("Enter your age: "))

create(name=name, pan_no=pan_no, number=number, age=age)

while True:
	print("\n1.deposite\n2.withdraw\n3.balance\n4.exit")
	op = int(input("Enter your Choice : "))
	print()
	if op == 1:
		d_amount = int(input("Enter deposit amount: "))
		deposit(d_amount)
	elif op == 2:
		w_amount = []
		while True:
		  		note = int(input("Enter withdrawal amount (0 to finish): "))
		  		if note == 0:
		  			break
		  		else:
		  			w_amount.append(note)
		withdraw(*w_amount) 
	elif op == 3:
		check_balance()
	else:
		break