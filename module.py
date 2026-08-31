print("***** WELCOME TO AREA CALCULATOR *****")
import math
radius = float(input("Enter the radius of the circle: "))
if (radius < 0):
    print("The radius cannot be negative! Try again.")
else:
    area = math.pi * math.pow(radius, 2)    
print(f"The area of circle with radius {radius} is {area:.2f}")    