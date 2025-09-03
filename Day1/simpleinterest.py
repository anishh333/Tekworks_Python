p=int(input("Enter the principal amount"))
t=int(input("Enter the total no of months"))
r=int(input("Enter the rate of interest"))
SI=(p*t*r)/100
print(f"Simple Interest is {SI:.2f} and total amount is {p+SI}")