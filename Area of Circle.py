# Calculating Area of a circle 1

print('Specify X to close the program')
while True:
    radius = input('Enter radius of Circle: ')

    if radius == 'X':
         break
    else:
        radius = float(radius)
        area = 3.14 * radius *radius
        print('The area of the Circle is: ' +str(area))
        
