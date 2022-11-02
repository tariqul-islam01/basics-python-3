matched_password: bool = False
input_password: str = ''
password: str = 'helloPwd'

while matched_password is not True:
    input_password = input('Please type your password!>>>')

    if input_password.lower() == password.lower():
        print('Congratualtions!!! your password matched')
        matched_password = True
    else:
        print('Oops! try again')


# alternative

while True:
    input_password = input('Please type your password!>>>')

    if input_password.lower() == password.lower():
        print('Congratualtions!!! your password matched')
        break
    else:
        print('Oops! try again')

print('Welcome ------')
