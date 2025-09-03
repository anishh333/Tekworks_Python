def even(a):
    if(a%2==0):
        return True
    else:
        return False

a=int(input("Enter a number"))
if(even(a)):
    print("Number is even")
else:
    print("Number is odd")

#nested if
def large(a,b,c):
    if(a>b):
        if(a>c):
            print(f"{a} is largest")
        else:
            print(f"{c} ids largest")
    else:
        if(b>c):
            print(f"{b} is largest")
        else:
            print(f"{c} is largest")
    
a=input("Enter a number ")
b=input("Enter a number ")
c=input("Enter a number ")
large(a,b,c)

#if-else
def vowel(a):
    s="aeiou"
    if(a in s):
        print("It is a vowel")
    else:
        print("It is a consonent")

def alphabet(a):
    if(a.isalpha()):
        print("It is a alphabet")
    else:
        print("It is not a aplhabet")
a=input("Enter a character ")
vowel(a)
alphabet(a)

#if-elif-else
def div(a):
    if(a%5==0 and a%11==0):
        print("Number is divisible by both 5 and 11")
    elif(a%5==0):
        print("NUmber is only divisible by 5")
    elif(a%11==0):
        print("Number is divisible by 11")
    else:
        print("Number is not divisible by any")
a=int(input("Enter a number "))
div(a)

#if-else
def maxi(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=maxi(a,b,c)
print(f"Maximum number among them is {d}")

#if-else
def leap(a):
    if(a%4==0 and a%100!=0) or(a%400==0):
        print("It is a leap year")
    else:
        print("It is not a leap year")

a=int(input("Enter a year"))
leap(a)
