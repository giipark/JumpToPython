"""
클래스
사각형의 가로와 세로 길이를 속성으로 갖는 클래스 Rectangle을 작성하세요.
또한 사각형의 넓이를 구하는 메서드 area()를 구현하세요.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rec = Rectangle(3, 4)
print(rec.area())