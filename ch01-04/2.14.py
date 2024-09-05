x1, y1 = eval(input("Enter the first coordinate for your triangle x1,y1: "))
x2, y2 = eval(input("Enter the second coordinate for your triangle x2,y2:"))
x3, y3 = eval(input("Enter the third coordinate for your triangle x3,y3:"))

side1 = ((x1-x2)** 2 +( y1-y2)**2)**0.5
side2 = ((x1-x3)** 2 +( y1-y3)**2)**0.5
side3 = ((x2-x3)** 2 +( y2-y3)**2)**0.5
s= (side1+side2+side3)/2

area= (s *(s-side1)*(s-side2)*(s-side3)) ** 0.5
print("The area of your triangle is:", area)