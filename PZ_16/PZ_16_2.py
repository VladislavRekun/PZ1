# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.
from math import pi


class Figure:

    def __init__(self, name:str, sides:tuple):
        self.sides = sides
        self.name = name

    def area(self):
        print(f"Неизвестная фигура {self.name}, невозможно определить площадь.")

    def perimeter(self):
        try:
            per = sum(self.sides)
        except:
            per = self.side * 4
        return per


fig1 = Figure('ABC', (3,4,5))
fig1.area()
print(f"Периметр {fig1.name} равен {fig1.perimeter()}")

class Square(Figure):

    def __init__(self, name:str, side):
        self.name =  name
        self.side = side

    def area(self):
        ar = self.side**2
        return ar

sq1 = Square('ABCD', 5)
print(f"Площадь квадрата {sq1.name} равна {sq1.area()}")
print(f"Периметр квадрата {sq1.name} равен {sq1.perimeter()}")

class Rectangle(Figure):

    def area(self):
        ar = self.sides[0] * self.sides[1]
        return ar

rect1 = Rectangle('BCED', (2,3))
print(f"Площадь прямоугольника {rect1.name} равна {rect1.area()}")
print(f"Периметр прямоугольника {rect1.name} равен {rect1.perimeter()}")

class Triangle(Figure):

    def area(self):
        p = self.perimeter() / 2
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        ar = (p*(p-a)*(p-b)*(p-c))**(1/2)
        return ar

tr1 = Triangle('BCD', (3,4,5))
print(f"Площадь треугольника {tr1.name} равна {tr1.area()}")
print(f"Периметр треугольника {tr1.name} равен {tr1.perimeter()}")

class Circle(Figure):

    def __init__(self, name:str, radius):
        self.name = name
        self.radius = radius

    def area(self):
        ar = self.radius**2 * pi
        return ar

    def perimeter(self):
        per = self.radius * 2 * pi
        return per

circ1 = Circle('Or', 5)
print(f"Площадь круга {circ1.name} равна {circ1.area()}")
print(f"Периметр круга {circ1.name} равен {circ1.perimeter()}")
