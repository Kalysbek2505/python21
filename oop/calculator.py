class Calc:
    def __init__(self, color):
        self.color = color

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def true_div(self, a, b):
        return a // b

    def mod(self, a, b):
        return a % b

    def divmod(self, a, b):
        return self.true_div(a, b), self.mod(a, b)

    def pow(self, a, b):
        return a ** b

    def sqrt(self, a, n_digits = 2):
        import math
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, n_digits)

    def percent(self, total, _percent):
        return (total * _percent) / 100

    def f

obj1 = Calc('синий')
obj2 = Calc('фиолетовый')

obj1.add(4,5)
obj2.add(4,5)
print(obj1)