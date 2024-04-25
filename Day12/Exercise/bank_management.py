class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

# Taking user input to create a BankAccount instance
account_number = input("Enter account number: ")
holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, holder_name, initial_balance)

# Interactive operations on the BankAccount object based on user input
while True:
    print("\n1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        account.display_balance()
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
                 
