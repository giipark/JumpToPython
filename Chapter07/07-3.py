for a in [1, 2, 3, 4]:
    print(a)
print("=" * 50)
# ================================================================================================
a = [1, 2, 3]
# next(a)   - 오류발생: TypeError: 'list' object is not an iterator
ia = iter(a)
print(type(ia))
print(next(ia))
print(next(ia))
print(next(ia))
# print(next(ia)) - 오류발생: StopIteration
print("=" * 50)
# ================================================================================================
a = [1, 2, 3, 4]
ia = iter(a)
for a in ia:
    print(a)

# iterator는 반복한 값을 다 읽으면 더 이상 그 값을 읽을 수 없음
for a in ia:
    print(a)
print("=" * 50)
# ================================================================================================
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))    - 오류발생: StopIteration