class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, new_point):
        return (((self.x - new_point.x) ** 2 + (self.y - new_point.y) ** 2)) ** 0.5

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show() 
point2.show()  

point1.move(3, 5)
point1.show() 

distance = point1.dist(point2)
print(f"Distance between points: {distance:.2f}") 
