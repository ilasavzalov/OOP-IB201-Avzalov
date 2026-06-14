class User:
    _counter = 0
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @classmethod
    def create(cls, name: str):
        cls._counter += 1
        return cls(cls._counter, name)
    
    @classmethod
    def count(cls) -> int:
        return cls._counter

print("Пример")
u1 = User.create("Ann")
u2 = User.create("Bob")
u3 = User.create("Cory")
print(u1.id, u2.id, u3.id)
print(User.count())
