"""
모듈
math 모듈을 사용하여 원의 넓이를 구하는 함수 circle_area를 작성하세요. 원의 반지름을 인자로 받습니다.
"""

from math import pi

def circle_area(radius):
    return pi * radius ** 2

print(circle_area(4))
