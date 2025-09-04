for i in range(6):
    for j in range(6):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5):
        if(j==i):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

for i in range(5):
    for j in range(5):
       print("$" if((j==i)or(i+j==4)) else "*",end=" ")
    print()

