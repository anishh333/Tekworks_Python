from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rect(Shape):
    def __init__(self,length:int,breadth:int):
        super().__init__()
        self.length=length
        self.breadth=breadth
    def area(self)->str:
        return f"Area is {self.length*self.breadth}"
class Circle(Shape):
    def __init__(self,radius:int):
        super().__init__()
        self.radius=radius
    def area(self)->str:
        return f"Area of circle is {3.14*self.radius**2}"

r1=Rect(10,20)
print(f"{r1.area()}")
c1=Circle(5)
print(f"{c1.area()}")