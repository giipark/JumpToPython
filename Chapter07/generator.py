def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result


g = mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

while True:
    try:
        print(next(g))
    except StopIteration:
        break
print("=" * 50)
# ================================================================================================
import sys

# generator expression
# 데이터를 한꺼번에 만들지 않고, 필요할 때마다 생성해서 메모리를 아낄 수 있음
gen_expr = (i * i for i in range(1, 1000))
print(type(gen_expr))
print(next(gen_expr))
print(list(gen_expr))  # next를 한번 했기때문에, 첫 번째 값인 1을 제외한 나머지가 리스트로 출력
print(f"Generator Expression 메모리 사용량: {sys.getsizeof(gen_expr)}")

# list comprehension
# 한 번에 모든 데이터를 리스트에 저장하므로 메모리를 더 많이 사용
list_comp = [i * i for i in range(1, 1000)]
print(type(list_comp))
print(list_comp)
print(f"List Comprehension 메모리 사용량: {sys.getsizeof(list_comp)}")
