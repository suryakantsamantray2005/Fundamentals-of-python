class Rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return (self.length + self.breadth)*2
    
    def area(self):
        return (self.length * self.breadth)
    
    def display(self):
        print("length is" ,self.length)
        print("breadth is",self.breadth)
        print("area is ",self.area())
        print("perimeter is",self.perimeter())
    
my_rectangle = Rectangle(3,4)
my_rectangle.display()