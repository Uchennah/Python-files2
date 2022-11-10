#Find the Largest of three Numbers


Count = 1 #a
print('Enter X to exit program')
print('Enter three numbers')
Number1 = input('Enter the first number: ')
if Number1 == 'X':
    exit()
else:
    Number1 = int(Number1)
    Number2 = int(input('Enter the second number: '))
    Number3 = int(input('Enter the third number: '))

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
   
    if (Number1 == Number2 and Number1 == Number3):
        Count = 0 #b
        if Count == 0: #c
           print('All the numbers are equal') #a,b,c can be removed from the code and we would still get a prompt that "All the numbers are equal"....
    else:                                     #...if the input by our user fulfils the 'if' statement. See HighestNumber2.py for code without the count variable.
        print('The highest number is: ' +str(HighestNum))

