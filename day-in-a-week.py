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