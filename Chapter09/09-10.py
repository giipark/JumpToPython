"""
파일 입출력
텍스트 파일을 생성하고, 다음 내용을 저장한 후 파일을 닫으세요.

Hello, world!
Welcome to Python.
"""

text = """Hello, world!
Welcome to Python."""

with open('0910.txt', 'w', encoding='utf-8') as f:
    f.write(text)