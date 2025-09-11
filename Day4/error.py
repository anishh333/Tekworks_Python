num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
try:
    c=num1/num2
    print(c)
except ArithmeticError:
    print("Division with zero is not allowed")