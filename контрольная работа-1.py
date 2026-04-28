# import math

# class Shape:
#     def __init__(self, color: str):
#         self._color = color

#     def area(self) -> float:
#         raise NotImplementedError

#     def describe(self) -> str:
#         raise NotImplementedError

# class Circle(Shape):
#     def __init__(self, color: str, radius: float):
#         super().__init__(color)  
#         self.radius = radius

#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError(f'Радиус должен быть числом')
#         self._radius = value

#     def area(self):
#         return math.pi * self.radius ** 2  
    
#     def describe(self):
#         return f'Перед нами круг {self._color} цвета с радиусом {self.radius} и площадью {self.area()}'


# class Rectangle(Shape):
#     def __init__(self, color, width: float, height: float):
#         super().__init__(color)  
#         self.width = width
#         self.height = height

#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError(f'Ширина должна быть числом')
#         self._width = value

#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError(f'Высота должна быть числом')
#         self._height = value

#     def area(self):
#         return self.width * self.height
    
#     def describe(self):
#         return f'Перед нами прямоугольник {self._color} цвета с шириной {self.width}, высотой {self.height} и площадью {self.area()}'


# def print_shapes(shapes: list):
#     for shape in shapes:
#         print(shape.describe())



