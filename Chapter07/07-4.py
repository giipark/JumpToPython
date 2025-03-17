a = 1
print("1:", type(a))

a = "1"
print('"1":', type(a))
print("=" * 50)
# ================================================================================================
num: int = 1
def add(a: int, b: int) -> int:
    return a + b

# 타입 어노테이션은 체크가 아닌 힌트!!
result = add(3, 3.4)    # 3.4는 float형 데이터지만, 사용가능
print(result)

"""
pip install mypy
 - mypy를 사용하면, 타입을 강제하여 오류를 감지할 수 있음

mypy 07-4.py 를 하게 되면
1. error: Incompatible types in assignment (expression has type "str", variable has type "int")
    - a가 int로 초기화 되었는데, str을 넣으려다보니 오류 발생
2. error: Argument 2 to "add" has incompatible type "float"; expected "int"
    - b는 int라고 힌트를 주었는데, float형 데이터를 입력하여 오류 발생
"""