class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    
    @classmethod
    def from_string(cls, s: str):
        # Убираем пробелы и разделяем по запятой
        parts = s.replace(' ', '').split(',')
        x = float(parts[0])
        y = float(parts[1])
        return cls(x, y)
    
    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["x"], d["y"])
    
    @staticmethod
    def distance(a, b):
        return round(((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5, 2)


p1 = Point.from_string("3, 4")
p2 = Point.from_dict({"x": 0, "y": 0})
print(p1.x, p1.y)
print(Point.distance(p1, p2))
