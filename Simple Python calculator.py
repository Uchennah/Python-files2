# Simple Python Calculator

def Addition(number1, number2):
    result = number1 + number2
    print('The result is: ' +str(result))
def Subtraction(number1, number2):
    result = number1 - number2
    print('The result is: '+str(result))
def Multiplication(number1, number2):
    result = number1 * number2
    print('The result is: ' +str(result))
def Division(number1, number2):
    result = number1/number2
    print('The result is: '+str(result))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. End')

while True:
    Operator = int(input('Enter desired Operator: '))
    if (Operator >=1 and Operator <=4):
        print('Enter Two Numbers')
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))
        
        if Operator == 1:
            Addition(number1,number2)
        elif Operator ==2:
            Subtraction(number1, number2)
        elif Operator == 3:
            Multiplication(number1,number2)
        else:
            Division(number1,number2)
    elif Operator == 5:
        break
        
    else:
        print('Operator entered is non-existent')
        print('Choose one of the available Operators')
          
    


