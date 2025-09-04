from math import sqrt,floor
a=int(input("Enter a number"))
for i in range(2,a+1):
    for j in range(2,floor(sqrt(i)+1)):
        if(i%j==0):
            break
    else:
        print(i)

def palin(a):
    b=0
    temp=a
    while(a>0):
        b=b*10+(a%10)
        a=a//10
    return b==temp
a=int(input("Enter a number"))
for i in range(1,a):
    if(palin(i)):
        print(i,end=" ")

def arm(a):
    temp=a
    b=0
    digits=len(str(a))
    while(temp>0):
        b+=((temp%10)**digits)
        temp//=10
    return a==b
a=int(input("Enter a number"))
print([i for i in range(1,a+1) if(arm(i))])

def strong(a):
    temp = a
    total = 0
    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        total += fact
        temp //= 10
    return a == total

a = int(input("Enter a number: "))
print(f"Strong numbers from 1 to {a}:")
for i in range(1, a + 1):
    if strong(i):
        print(i, end=" ")

def prefect(a):
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum+=i
    return sum==a
a=int(input("Enter a number"))
for i in range(1,a+1):
    if(prefect(i)):
        print(i,end=" ")

def factors(a):
    for i in range(1,a+1):
        if(a%i==0):
            print(i,end=" ")
a=int(input("Enter a number"))
factors(a)
from math import sqrt

# Function to check if a number is prime
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factors(a):
    print(f"Prime factors of {a}: ", end="")
    for i in range(2, a + 1):
        if isPrime(i) and a % i == 0:
            print(i, end=" ")
    print()

a = int(input("Enter a number: "))
factors(a)

a=int(input("Enter a number"))
fib=[0,1]
for i in range(a):
    n=len(fib)
    fib.append(fib[n-1]+fib[n-2])
for i in range(len(fib)):
    print(fib[i],end=" ")
