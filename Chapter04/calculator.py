# calculator.py
import sys


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return 0
    return x / y


if len(sys.argv) != 4:
    print("사용법: calculator.py 숫자1 연산자 숫자2")
else:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    if operator == '+':
        print(f"{num1} {operator} {num2} = {add(num1, num2)}")
    elif operator == '-':
        print(f"{num1} {operator} {num2} = {minus(num1, num2)}")
    elif operator == '*':
        print(f"{num1} {operator} {num2} = {multiply(num1, num2)}")
    elif operator == '/':
        print(f"{num1} {operator} {num2} = {divide(num1, num2)}")
    else:
        print("지원하지 않는 연산자입니다. 사칙연산 기호(+, -, *, /)를 입력해주세요.")
        sys.exit(1)
