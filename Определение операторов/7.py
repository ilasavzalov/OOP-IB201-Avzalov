class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients[:]
    
    def __call__(self, x):
        result = 0
        for power, coef in enumerate(self.coefficients):
            result += coef * (x ** power)
        return result
    
    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefs = [0] * max_len
        
        for i in range(len(self.coefficients)):
            new_coefs[i] += self.coefficients[i]
        
        for i in range(len(other.coefficients)):
            new_coefs[i] += other.coefficients[i]
        
        return Polynomial(new_coefs)


print("Пример1")
poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))
print()

print("Пример2")
poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()
print()

print("Пример3")
poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
