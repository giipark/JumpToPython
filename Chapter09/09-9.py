"""
리스트 내포
1부터 10까지의 제곱값을 갖는 리스트를 생성하세요.
"""

# 1번
result = []
for i in range(1, 11):
    result.append(i ** 2)
print(result)

# 2번
result = [i ** 2 for i in range(1, 11)]
print(result)