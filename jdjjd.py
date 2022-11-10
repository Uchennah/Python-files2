import random
secret_number = random.randint(1,20)
print('I am thinking of a number')

for i in range(1,4)
print('Try to guess the number')
guess = int(input('Enter Number between 1 and 20:  '))

if guess < secret_number:
    print('The specified number is low')

elif guess > secret_number:
    print('The number specified is high')

else:
    break

if guess == secret_number:
    print('Congratulation you have guessed the number')

else:
    print('Better luck next time! The correct number was:  ' + str(secret_number)) )
