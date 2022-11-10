#Find the largest of three numbers


def checkForHighestNum(Number1,Number2,Number3):
    global HighestNum
    HighestNum = Number1
    if HighestNum < Number2:
        if Number2 > Number3:
            HighestNum = Number2
        else:
            HighestNum = Number3
    elif HighestNum < Number3:
        if Number3 > Number2:
            HighestNum = Number3
        else:
            HighestNum = Number2
    else:
        HighestNum = Number1
    

count = 1
print('Enter X to exit program')
print('Enter three numbers')
Number1 = input('Enter the first number: ')
if Number1 == 'X':
    exit()
else:
    Number1 = int(Number1)
    Number2 = int(input('Enter the second number: '))
    Number3 = int(input('Enter the third number: '))
    checkForHighestNum(Number1,Number2,Number3)
    if (Number1 == Number2 and Number1 == Number3):
        count = 0 #This part1 can be removed and code would still run well
    if count == 0: #Part2 as well can be removed. Check HighestNumber2.py
         print('All the numbers are equal')
    else:
        print('The highest number is: ' +str(HighestNum))
                                                 
                  

   
