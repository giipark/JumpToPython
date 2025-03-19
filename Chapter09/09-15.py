"""
상속
위에서 작성한 Rectangle 클래스를 상속받아 정사각형을 나타내는 Square 클래스를 작성하세요.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square = Square(4)
print(square.area())