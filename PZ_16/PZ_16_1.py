# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.

class Calculator:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        result = self.num1 / self.num2
        return result

calculate1 = Calculator(4,2)
print(calculate1.add())
print(calculate1.sub())
print(calculate1.mul())
print(calculate1.div())


