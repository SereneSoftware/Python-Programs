def fact(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return n * fact(n-1)
print("**** WELCOME TO FACTORIAL.PY ****")
c = int(input("Enter the number to get it's factorial: "))
x = fact(c)
print(x)