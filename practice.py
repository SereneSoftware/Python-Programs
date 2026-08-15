'''fav_food = input("Enter your fav food: ")
print("Wow! I also like", fav_food)
print("Well, did you know the word", fav_food, "you entered was", type(fav_food), "datatype!")

print('Harry said, "Python is awesome!"\nThis is on a new line.\nThis is a tab ->\t<- here')

num = int(input("Enter the number: "))
square = num ** 2
cube = num ** 3
print("The cube of", num, "is: ", cube, "\nThe square of", num, "is: ", square)
print('Harry said, "Python is awesome!"\nThis is on a new line.\nThis is a tab ->\t<- here')

x = int(input("Enter a number: "))
if (x == 0):
    print("Given number is 0.")
elif(x < 0):
    print(x, "is negative.")
else:
    print(x, "is positive")    

day = int(input("Enter a number(0-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")   
    case 3:
        print("Wednesday")   
    case 4:
        print("Thursday")    
    case 5:
        print("Friday")      
    case 6:
        print("Saturday")    
    case 7:
        print("Sunday")   
    case _:
        print("Please choose a number between 0 to 7")   

age = int(input("Enter your age: "))
if (age < 18):
    print("You are not eligible to vote.")
else:
    print("You can vote.")

x = int(input("Enter a number: "))
if (x%2 == 0):
    print(x, "is even number.")
else:
    print(x, "is odd number.")  

for i in range(1, 11):
    print(i)

total = 0
for i in range(1, 101):
    total += i
print("sum: ", total)    

for i in range(1, 6):
    for j in range(i):
        print("*")
        print(end=" ")    
 
total = 0 
i = 1 
while (i <= 100):
    total += i
    i += 1
print(total)    

'''
