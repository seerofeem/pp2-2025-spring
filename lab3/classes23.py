class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

leng = float(input("Enter the length: "))
widt = float(input("Enter the width: "))
shape = Shape()
print("Area of Shape:", shape.area())  
square = Square(leng)
print("Area of Square:", square.area()) 
rectangle = Rectangle(leng, widt)
print("Area of Rectangle:", rectangle.area())