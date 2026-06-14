from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
    
    def area(self) -> int:
        return self.w * self.h
    
    def set_width(self, w: int) -> None:
        self.w = w
    
    def set_height(self, h: int) -> None:
        self.h = h
    
    def get_width(self) -> int:
        return self.w
    
    def get_height(self) -> int:
        return self.h


class Square(Shape):
    def __init__(self, side: int):
        self.side = side
    
    def area(self) -> int:
        return self.side * self.side
    
    def set_side(self, side: int) -> None:
        self.side = side
    
    def get_side(self) -> int:
        return self.side


def resize_and_get_area(rect: Rectangle) -> int:
    rect.set_width(10)
    rect.set_height(5)
    return rect.area()


rect = Rectangle(1, 1)
print(resize_and_get_area(rect))

square = Square(5)
square.set_side(10)
print(square.area())
