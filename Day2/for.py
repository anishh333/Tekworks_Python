#table
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
a=int(input("Enter a number"))
table(a)

#sum of digits
a=int(input("Enter a number "))
sum=0
while(a>0):
    sum+=a%10
    a//=10
print(sum)

a=int(input("Enter a number"))
sum=0
while(a>0):
    sum+=1
    a//=10
print(sum)

a=int(input("Enter a number"))
s=a
while(s>10):
    s//=10
print(f"{s},{a%10}")
print(f"Sum is {s+(a%10)}")

for i in range(256):
    print(f" {i}->{chr(i)}")

def number_to_words(num):
    digits_map = {
        '0': "zero",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }
    
    result = " ".join(digits_map[d] for d in str(num))
    return result



num =int(input("Enter a number "))
print(number_to_words(num))  
