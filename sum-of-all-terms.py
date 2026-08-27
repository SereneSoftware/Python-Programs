def sum(n):
    if (n==0):
        return 0
    else:
        return n + sum(n-1)

print("*-*-* WELCOME TO SUM THE TERMS *-*-*")
x = int(input("Enter the number of terms to sum: "))
print(f"The sum of numbers till {x} is {sum(x)}")   