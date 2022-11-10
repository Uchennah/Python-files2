import random

secretNumber = random.randint(1,15)
print('I just thought of a number')

def guess_number():
    global guess
    for i in range(1,5):
        print('Try to guess the number')
        guess = float(input('Enter any number between 1 and 15: '))
        if guess < secretNumber:
            print('The number specified is too low')
        elif guess > secretNumber:
            print('The number specified is too high')
        elif guess/secretNumber == float(secretNumber) : 
            print('The number is a whole Number')
        else:
            break
         

        
    
guess_number()     
if guess == secretNumber:
     print('Congratulations you have guesseed the number')
else:
     print('Better Luck NextTime!  The correct number is:' +str(secretNumber))


    
                
                
