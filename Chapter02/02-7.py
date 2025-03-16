from encodings.quopri_codec import quopri_encode
from typing import List

# bool
# True: 참
# False: 거짓

a = True
b = False
print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(3 < 1)

a = [1, 2, 3, 4]
while a:
    print(a.pop())

# help(list.pop)    - list.pop 함수의 설명
# print(dir(list))  - list가 제공하는 모든 메서드를 확인할 수 있음
print("=" * 50)
if []:
    print("TRUE")
else:
    print("FALSE")
if [1, 2, 3]:
    print("TRUE")
else:
    print("FALSE")

print("=" * 50)
print(bool('Python'))  # True
print(bool(''))  # False
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool(0))  # False
print(bool(3))  # True
