num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter the operator(*, -, +, /): ")
match operator:
    case "*":
        print(num1, "*", num2, "=", num1*num2)
    case "-":
        print(num1, "-", num2, "=", num1-num2)
    case "+":
        print(num1, "+", num2, "=", num1+num2)
    case "/":
        print(num1, "/", num2, "=", num1/num2)    