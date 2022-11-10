import random

def getNumber (Number):
    if Number == 1:
        return 'The number is 1'
    elif Number == 2:
        return 'The number is 2'
    elif Number == 3:
        return 'The number is 3'
    elif Number == 4:
        return 'The number is 4'
    elif Number == 5:
        return'The number is 5'
    random_number = random.randint(1,5)
    pick = getNumber(random_number)
    print('pick')
