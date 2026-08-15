print("-------   MATHEMATICAL TABLE PRINTER   -------")
num = int(input("Enter a number(1 to 5) to print their mathematical table: "))
match num:
    case 1:
        for i in range(1, 11):
            print("1 X", i, "=", 1*i)
    case 2:    
        for i in range(1, 11):
            print("2 X", i, "=", 2*i)    
    case 3:
        for i in range(1, 11):
            print("3 X", i, "=", 3*i)
    case 4:
        for i in range(1, 11):
            print("4 X", i, "=", 4*i)                
    case 5:
        for i in range(1, 11):
            print("5 X", i, "=", 5*i)   
    case _:
        print("Please select from given numbers.")           
print("..... THANKYOUU ......")              