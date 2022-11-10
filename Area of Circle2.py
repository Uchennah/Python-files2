#Calculating the Area of a Circle 2

def calculate_radius(radius):
    radius = float(radius)
    area = 3.14 * radius * radius
    print('The area of the Circle is: ' +str(area))

print('Specify X to end program')
  


while True:
    radius = input('Enter the radius of the Circle: ')
    if radius == 'X':
        break
    calculate_radius(radius)
