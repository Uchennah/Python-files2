import random

secretNumber = random.randint(1,20)
print("I am currently thinking of a number")

for i in range (1,4):
    print('Try to guess the Number')
    guess = int(input('Enter numbers between 1 and 20: '))

    if guess < secretNumber:
        print('The number specified is too Low')
    elif guess > secretNumber:
        print('The number specified is too High')
    else:
        break

if guess == secretNumber:
    print('Congratulations you have guessed the number')
else:
    print('Better luck next time! The correct number was: '+str(secretNumber))















        








              
