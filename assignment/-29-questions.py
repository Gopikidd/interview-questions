#29. Write a function that takes the radius of a circle as input and returns its area.

def area_circle(r):
    pi = 3.14
    area = pi*r**2

    print('RADIUS OF CIRCLE = ', area, 'mm')

radius = int(input('enter the radius = '))

area_circle(radius)
