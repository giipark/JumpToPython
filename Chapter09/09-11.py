"""
예외 처리
정수를 입력받아 10을 나누는 코드를 작성하세요. 0으로 나누는 경우에 대한 예외 처리를 포함하세요.
"""

try:
    num = int(input("정수를 입력해주세요: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
