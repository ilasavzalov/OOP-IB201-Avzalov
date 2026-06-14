class Summator:
    def transform(self, n):
        return n
    
    def sum(self, N):
        total = 0
        for i in range(1, N + 1):
            total += self.transform(i)
        return total

class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2

class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
