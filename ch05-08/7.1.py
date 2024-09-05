class Rectangle:
    def __init__(self,width=1,height=2):
        self.width = width
        self.height= height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width+self.height)*2


rec1= Rectangle(4,40)
rec2= Rectangle(3.5,35.7)
area1= rec1.getArea()
area2= rec2.getArea()
per1= rec1.getPerimeter()
per2= rec2.getPerimeter()


print("Rectangle 1:\n\tWidth =",rec1.width,"\n\tHeight =",rec1.height,"\n\tArea =",area1,"\n\tPerimeter =",per1)
print("Rectangle 2:\n\tWidth =",rec2.width,"\n\tHeight =",rec2.height,"\n\tArea =",area2,"\n\tPerimeter =",per2)
