# 7. Реализовать проект «Операции с комплексными числами».

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f"{self.a} - {abs(self.b)}i"
        else:
            return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


n1 = Complex(1, -2.5)
n2 = Complex(-3, 5)
print(n1)
print(n2)
print(n1 + n2)
print(n1 * n2)
