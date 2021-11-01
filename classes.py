from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass



class Square(Shape):
    def area(self, x):
        return x*x
    def perimeter(self, x):
        return 4*x


class Rectangle(Shape):
    def area(self, x, y):
        return x * y

    def perimeter(self,x,y):
        return 2*(x+y)

shape = Rectangle()
print(shape.area(6,7))