s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)  # 순서가 랜덤하게 출력

s = set()
print(s)

s.add(1)
s.add("one")
print(s)
print("=" * 50)

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])
l1[0] = 4
print(l1)

t1 = tuple(s1)
print(t1)
print(t1[0])
print("=" * 50)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
# print(a - b)    - 오류발생: TypeError: unsupported operand type(s) for -: 'list' and 'list'
print("=" * 50)

s1 = set([1, 2, 3])
s1.add(4)
print(s1)
s1.update([5, 6, 7, ])  # 트레일링 콤마(Trailing Comma) / 마지막에 쉼표 있어도 에러 없음!
print(s1)
s1.remove(7)
print(s1)

for num in [5, 6, 7]:
    s1.discard(num)  # 없는 요소를 삭제하려 해도 에러가 나지 않음.
print(s1)   # s1 = {1, 2, 3, 4}

s1.symmetric_difference_update([3, 4, 5])   # 차집합(Symmetric Difference)를 구하고, 원본 set을 업데이트 / "겹치지 않는 요소들"만 남기는 연산
# s1.difference_update([3, 4, 5])
print(s1)

s1 -= {1, 2}
print(s1)

print("=" * 50)
tup1 = (1)  # tuple이 아니라 정수(int)로 인식됨!  (요소가 하나일때는 꼭 ,를 붙여야함)
print(type(tup1))
tup1 = (1,)  # tuple
print(type(tup1))
