r=int(input("Enter the radius of circle"))

print(f"The area of circle is {3.14*r*r}sqcm and circumference is {2*3.14*r}cm")

#cylinder
h=int(input("Enter the height of cylinder"))
r=int(input("Enter the radius of cylinder"))
v=3.14*r*r*h
print(f"Volume of cylinder is {v:.2f}")

#Rectangle
length=int(input("Enter length of the Rectangle"))
breadth=int(input("Enter breadth of the rectangle"))
print(f"The area of rectangle is {length*breadth} and circumference is {2*(length+breadth)}")

#cube
a=int(input("Enter the length of any side of cube"))
print(f"The volume of cube {a**3}")
