class Employee:
    def __init__(self,name:str,salary:int):
        self.name=name
        self.salary=salary
    def display(self):
        print(f" Name : {self.name}\n Salary : {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary,dept:str):
        super().__init__(name, salary)
        self.dept=dept
    def display(self):
        super().display()
        print(f" Department : {self.dept}")
m1=Manager("Anish",750000,"SDE")
m1.display()
e1=Employee("Bhargav",60000)
e1.display()