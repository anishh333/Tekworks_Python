class Student:
    def __init__(self,name:str,rollno:int,marks:int):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f" Name : {self.name} \n RollNo : {self.rollno} \n Marks : {self.marks}")
    def __str__(self):
        return f"{self.name}->{self.rollno},{self.marks}"

print("---------------Student Details-------------")
std1=Student("Anish",21,99)
std1.display()
print("---------------Student Details-------------")
std2=Student("Bhargav",34,35)
std2.display()
print("---------------Student Details but with str fun-------------")
print(std1)
print("---------------Student Details but with str fun-------------")
print(std2)