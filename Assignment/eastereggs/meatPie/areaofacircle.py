#asks for the radius and prints the area of a circle

print(' Calculate the area of a Circle ')
radius = int(input("Enter the radius: "))

radius_square = radius * radius
pi = 3.142

area = pi * radius_square

print(f"The area of the Circle = {area}")
