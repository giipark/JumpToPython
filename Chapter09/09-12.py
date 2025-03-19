"""
람다 함수
주어진 리스트의 각 요소에 2를 곱하는 람다 함수를 작성하고, map() 함수를 사용해 결과를 출력하세요.

numbers = [1, 2, 3, 4, 5]
"""

numbers = [1, 2, 3, 4, 5]

# 1번 - map() 함수 사용
print(list(map(lambda x: x * 2, numbers)))

# 2번
result = [lambda x: x * 2 for i in numbers]
print(result)
