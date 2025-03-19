"""
정규 표현식
주어진 문자열에서 숫자만 추출하여 리스트로 저장하세요.

text = "Phone number: 010-1234-5678, age: 25"
"""
import re

text = "Phone number: 010-1234-5678, age: 25"
result = [re.findall('[0-9]+', text)]
print(result)