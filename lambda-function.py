print("*** WELCOME TO FINDING SQUARE AND CUBE OF A NUMBER ***")
x = int(input("Enter the number to sqaure it: "))
y = int(input("Enter the number to cube it: "))
square = lambda x: x*x
cube = lambda y: y*y*y
print(f"The square of {x} is {square(x)}")
print(f"The cube of {y} is {cube(y)}")