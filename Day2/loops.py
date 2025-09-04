def naturals(n):
    i=1
    while(i<=n):
        print(i)
        i=i+1
n=int(input("Enter a number"))
naturals(n)

#print all characters
for ch in range(ord('a'), ord('z') + 1):
    print(chr(ch), end=' ')

a=int(input("Enter a number"))
sum=0
for i in range(a+1):
    sum+=i
print(sum)

a=int(input("Enter a number"))
fact=1
for i in range(a,0,-1):
    fact*=a
    a-=1
print(fact)
from math import sqrt
def isPrime(a):
    i=2
    while i<=sqrt(a):
        if(a%i==0):
            print("Not a prime")
            break
        i=i+1
    else:
        print("Is Prime")

a=int(input("Enter a number"))
isPrime(a)

