"""
문자열 조작
주어진 문자열에서 모든 공백을 제거하고 역순으로 출력하세요.

text = "Python is fun!"
"""

text = "Python is fun!"
print(text.replace(' ', '')[::-1])