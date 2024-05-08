import datetime
#importing datetime module to get login date&time
user_name = []
password = []
date = []

while (un := input('Enter user name (e for exit):')) != 'e':
    user_name.append(un)
    password.append(input('Enter password :'))
    date.append((datetime.date.today()))

login_details = zip(user_name, password, date)

for user, passw, login_date in login_details:
    print(f'In {login_date} User : {user}\nLogin with password : {passw}')