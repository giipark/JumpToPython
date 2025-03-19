"""
문자열 조작
주어진 문자열에서 대문자와 소문자를 서로 바꾼 결과를 출력하세요.

text = "PythonIsFun"
"""

text = "PythonIsFun"

# 1번
result = ""
for t in text:
    if t.isupper():
        result += t.lower()
    elif t.islower():
        result += t.upper()
print(result)

# 2번
result = []
for t in text:
    if t.isupper():
        result.append(t.lower())
    elif t.islower():
        result.append(t.upper())
print("".join(result))

# 3번
print(text.swapcase())