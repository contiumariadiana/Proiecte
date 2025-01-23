import math

class Shape:
    def area(self):
        """
        Returnează aria formei geometrice.
        """
        raise NotImplementedError("Subclasele trebuie să implementeze metoda area().")

class Circle(Shape):
    def __init__(self, radius):
        """
        Inițializează un cerc cu raza specificată.
        :param radius: Raza cercului.
        """
        self.radius = radius

    def area(self):
        """
        Calcularea ariei cercului.
        """
        return math.pi * self.radius ** 2

    def __str__(self):
        """
        Reprezentare textuală a cercului.
        """
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Inițializează un dreptunghi cu lățimea și înălțimea specificate.
        :param width: Lățimea dreptunghiului.
        :param height: Înălțimea dreptunghiului.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcularea ariei dreptunghiului.
        """
        return self.width * self.height

    def __str__(self):
        """
        Reprezentare textuală a dreptunghiului.
        """
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

# Exemplu de utilizare:
circle = Circle(5)
rectangle = Rectangle(10, 4)

print(circle)  # "Circle with radius 5 has area 78.54"
print(rectangle)  # "Rectangle with width 10 and height 4 has area 40"