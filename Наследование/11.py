class Summator:
    def transform(self, n):
        return n
    
    def sum(self, N):
        total = 0
        for i in range(1, N + 1):
            total += self.transform(i)
        return total

class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b
    
    def transform(self, n):
        return n ** self.b

class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)

class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)
