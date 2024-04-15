s = int(input("Enter Stack Size : "))
stack = []

while True:
        print("\n**MENU**\n1:push\n2:pop\n3:display")
        op = int(input("Enyer your Choice (0 for exit) : "))
        print()

        if op==1:
                if len(stack) == s:
                        print("Stack Overflow!")
                else:
                        stack.append(int(input("Enter Value : ")))

        elif op==2:
                if len(stack)==0:
                        print("Stack Underflow!")
                else:
                        print(stack[len(stack)-1],"is deleted!")
                        stack.pop(len(stack)-1)

        elif op==3:
                if len(stack)==0:
                        print("Stack is empty!")
                else:
                        print("Stack Elements :",stack)

        elif op==0:
                break

        else:
                print("Select a valid option!")
