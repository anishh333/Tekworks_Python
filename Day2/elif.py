def week(a):
    if(a==1):
        return "Monday"
    elif(a==2):
        return "Tuesday"    
    elif(a==3):
        return "Wednesday"
    elif(a==4):
        return "Thursday"
    elif(a==5): 
        return "Friday"
    elif(a==6):
        return "Saturday"
    elif(a==7):
        return "Sunday"
    else:
        return "Invalid Input"
    
a=int(input("Enter a number between 1-7: "))
print(week(a))

#checking whether the character is alphabet, digit or special character
def character(a):
    if(a.isalpha()):
        return "Alphabet"
    elif(a.isdigit()):
        return "Digit"
    else:
        return "Special Character"
    
a=input("Enter a character: ")
print(character(a))

#Student Details with Grade
stid=int(input("Enter the student id"))
sname=input("Enter the name os the Student")
marks_m=int(input("Enter the math marks of student"))
marks_p=int(input("Enter the phy marks of student"))
marks_c=int(input("Enter the chem marks of student"))
total=marks_c+marks_m+marks_p
avg=total/3
if(avg<40 or marks_c<40 or marks_m<40 or marks_p<40):
    Grade="Fail"
else:
    if(avg<=50 and avg>40):
        Grade="C"
    elif(avg>51 and avg<70):
        Grade="B"
    elif(avg>71 and avg<80):
        Grade="A"
    else:
        Grade="Distension"
print("Student Detils :")
print("Id:",stid)
print("Name:",sname)
print("Math marks : ",marks_m)
print("Phy marks : ",marks_p)
print("Chem marks : ",marks_c)
print("Total marks : ",total)
print(f"Average marks : {round(avg,2)}")
print(f"Grade of student is {Grade}")

#Current Bill 
c_no = int(input("Enter the customer number: "))
c_name = input("Enter the customer name: ")
pmr = int(input("Enter present month reading: "))
lmr = int(input("Enter last month reading: "))

total_units = pmr - lmr
def curr(total):
    bill=0
    if(total<50):
        bill=total*3.8
    elif(total>50 and total<100):
        bill=50*3.8+(total-50)*4.2
    elif(total>100 and total<200):
        bill=50*3.8+50*4.2+(total-100)*5.1
    elif(total>200 and total<300):
        bill=50*3.8+50*4.2+100*5.1+(total-200)*6.3
    elif(total>300):
        bill=50*3.8+50*4.2+100*5.1+100*6.3+(total-300)*7.5

    return bill

print("-----------------------------------Customer Details------------------------------")
print(f"Number: {c_no}")
print(f"Name: {c_name}")
print(f"Last Month Reading: {lmr}")
print(f"Current Month Reading: {pmr}")
print(f"Total Units used: {total_units}")
print(f"Current Bill: {round(curr(total_units), 2)}")

#total no of notes
def notes(a):
    dict={
        "2000":0,
        "500":0,
        "100":0,
        "50":0,
        "10":0,
        "1":0
    }
    if(a>=2000):
        dict["2000"]=a//2000
        a=a%2000
    if(a>=500):
        dict["500"]=a//500
        a=a%500
    if(a>=100):
        dict["100"]=a//100
        a=a%100
    if(a>=50):
        dict["50"]=a//50
        a=a%50
    if(a>=10):
        dict["10"]=a//10
        a=a%10
    if(a>=1):
        dict["1"]=a//1
    return dict
a=int(input("Enter amount"))
n=notes(a)
for key,value in n.items():
    print(f"{key}:{value}")