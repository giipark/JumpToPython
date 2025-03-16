# calculator.py
def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        return a / b
