import random

def guess_number():
    global guess
    for i in range(1,4):
        print('Try to guess the Number')
        guess = int(input('Enter a Number bewteen 1 and 20: '))
       

        if guess < secretNumber:
            print('The Number specified is too Low')
        elif guess > secretNumber:
            print('The Number specified is too High')
        else:
            break
    
                                
secretNumber = random.randint(1,20)
print('I an thinking of a Number')
guess_number()

if guess == secretNumber:
    print('Congratulation you have guessed the Number')
else:
    print('Better luck next time!  The correct Number is:  ' +str(secretNumber))
    
            
            
