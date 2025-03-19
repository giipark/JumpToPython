"""
함수와 리스트
주어진 리스트에서 홀수만 추출하여 새로운 리스트를 생성하는 함수 get_odd_numbers를 작성하세요.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1번
def get_odd_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result
print(get_odd_numbers(numbers))

# 2번
def get_odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]
print(get_odd_numbers(numbers))