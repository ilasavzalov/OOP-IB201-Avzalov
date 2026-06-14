class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
    def intersection(self, other):
        # Вычисляем координаты пересечения
        left = max(self.x, other.x)
        right = min(self.x + self.w, other.x + other.w)
        bottom = max(self.y, other.y)
        top = min(self.y + self.h, other.y + other.h)

        if left < right and bottom < top:
            # Создаём и возвращаем новый прямоугольник
            return Rectangle(left, bottom, right - left, top - bottom)
        else:
            return None

print("Пример1")
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())

print("Пример2")
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())



print("Пример3")
rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
