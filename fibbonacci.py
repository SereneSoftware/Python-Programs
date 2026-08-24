def fib(n):
    if(n == 1 or n == 0):
        return n
    elif (n < 0):
        return "Term should be positive"
    else:
        return fib(n-2) + fib(n-1)

x = int(input("Enter the number of terms: "))
y = fib(x)
print(f"The {x}th Fibonacci number is {y}")