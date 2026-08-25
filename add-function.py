print("***** WELCOME TO ADD THE NUMBER *****")
print("HERE WE ADD 5 TO ANY 2 NUMBERs YOU PICK")
def  add(a, b, default=5):
    addition = a +b + default
    return f"The addition of {a}, {b}, and {default} is {addition}"

x = int(input("Enter a: "))
y = int(input("Enter b: "))
addition1 = add(x, y)
print(addition1)