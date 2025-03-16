from faker import Faker

fake = Faker()
print(fake.name())

fake = Faker('ko-KR')
print(fake.name())

print(fake.address())

test_data = [
    (fake.name(), fake.address(), fake.postcode(), fake.country(), fake.company(), fake.email(), fake.phone_number())
    for _ in range(30)]
for i, *data in enumerate(test_data, start=1):
    print(f"{i}. {' - '.join(map(str, data))}")
print("=" * 50)
# ================================================================================================
from fractions import Fraction
import sympy

x, y = sympy.symbols("x y")

f = sympy.Eq(x*Fraction('2/5'), 1760)
print(f)

a = Fraction(1, 5)
print(a)
a = Fraction('1/5')
print(a)

result = sympy.solve(f)
print(result)
remains = result[0] - 1760
print(f"남은 돈은 {remains}원")
print("=" * 50)
# ================================================================================================
f = sympy.Eq(x**2, 1)
result = sympy.solve(f)
print(f"x**2 = 1의 해는 {result}")
print("=" * 50)
# ================================================================================================
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
result = sympy.solve([f1, f2])  # 연립방정식
print(result)   # 미지수가 2개 이상이면 Dictionary 타입으로 반환