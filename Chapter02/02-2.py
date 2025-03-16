a = "{0:=^10}".format("hi")
print(a)
print("{0:x<10}".format(77))
print("{0:=+10}".format(42))   # 기본 (공백으로 채움)
print("{0:*=+10}".format(42))  # '*'로 채움
print("{0:0=+10}".format(42))  # '0'으로 채움 (일반적인 숫자 패딩)

print("{0:0.4f}".format(3.141592869))


name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

print(f"난 {1500000:,}원이 필요해")
print(f"난 {1500000:_}원이 필요해")
print(f"난 {1500000:.2f}원이 필요해")
print(f"난 {1500000:,.0f}원이 필요해".replace(",", " "))
print(f"난 {1500000:_.0f}원이 필요해".replace("_", " "))
print(f"난 ₩{1500000:,}원이 필요해")

a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('i'))
print(a.find('z'))

print(a.index('i'))
# print(a.index('z')) - 오류 발생: ValueError: substring not found

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))
print(a.upper())
print(a.lower())

a = "   hi   "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a.replace("hi", "hello"))

a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))