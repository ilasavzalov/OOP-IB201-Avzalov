class Shape:
    _registry = {}
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Shape._registry[cls.__name__] = cls
    
    @classmethod
    def available(cls) -> list:
        return sorted(Shape._registry.keys())


class Circle(Shape):
    pass


class Square(Shape):
    pass


class Triangle(Shape):
    pass


print(Shape.available())
