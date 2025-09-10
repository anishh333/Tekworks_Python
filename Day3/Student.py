#A school stores records as tuples of (name, age, marks).
def std()-> tuple:
    name=input("Enter the name")
    roll=int(input("Enter the roll no of Student"))
    marks=int(input("Enter the marks of Student"))
    return (name,roll,marks)
def marksmax(li:list)->tuple:
    max=0
    name=""
    for i in li:
        if max<i[2]:
            max=i[2]
            name=i[0]
    return (name,max)
def std_pass(li:list)->list:
    ltn=[]
    for i in li:
        if i[2]>75:
            ltn.append(i[0])
    return ltn
lt=[]
for i in range(5):
    lt.append(std())
print(f"Student with maximum marks is {marksmax(lt)}")
print(f"Student with above 75 marks are {std_pass(lt)}")
