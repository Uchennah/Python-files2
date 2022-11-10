#true loop
password= "Hello world"
input_password = input('enter password: ')
while input_password !=password:
    input_password = input('Enter password: ')
    if input_password == password:
        break

    
print('Correct password')
