def calculate_area(length, width=10):
    area = length * width
    return area
print("***** WELCOME TO CALCULATE AREA *****")
x = int(input("Enter the length of the rectangle (in cm): "))
y = int(input("Enter the breadth of the rectangle (in cm): "))
print(f"The area of rectangle is {calculate_area(x,y)} cm")