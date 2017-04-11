print('LOGIN')
user = input('Insert the user: ')
password = input('Insert the password: ')

while user == password:
    print('Invalid Credentials.\nLOGIN')
    user = input('Insert the user: ')
    password = input('Insert the password: ')
