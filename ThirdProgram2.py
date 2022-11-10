inputedpassword = input('Enter Password:')
inputedpassword = str(inputedpassword)
Password = 'Password132'
Passkey = 'massword132'
if inputedpassword == Password:
    print('Correct Password... Access Granted')
elif inputedpassword == Passkey:
    print('Wrong Password... Access Denied')
else:
    print('Click link below to change password')
