# User input
mail = input("Enter Your Email : ")

# Conditional statement
if mail.count("@") == 1:
    # String manipulation
    index = mail.index("@")
    user_name = mail[:index]
    domain = mail[index+1:]
    
    # Nested conditional statement
    if domain == "gmail.com":
        # Output
        print(f"\nYour User Name is *{user_name}*")
        print(f"Your domain is *{domain}*")
    else:
        # Output
        print(f"*{domain}* domain  is incorrect! check it again")
else:
    # Output
    print(f"Your Email *{mail}* is incorrect! we can't find @ in your mail")
