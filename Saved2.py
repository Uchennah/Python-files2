import random

secretNumber= random.randint(1,20)
print('I thought of a number')

def guess_number():
    global guess
    for i in range(1,4):
        print('Try to guess the number')
        guess=int(input('Enter a number between 1 and 20: '))

        if guess<secretNumber:
            print('Number specified is to Low')
        elif guess>secretNumber:
           print('Number specified is too High')
        else:
            break
        
                   
        
    return guess

def check(guess, secretNumber):
    if guess==secretNumber:
        print('Congratulations, you have guessed the number')
    else:
        print('Better luck next time! The correct number is: ' +str(secretNumber))


guess=guess_number()
check(guess, secretNumber)
