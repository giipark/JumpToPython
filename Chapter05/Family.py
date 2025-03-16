class Family:
    lastname = "김"  # 클래스 변수

print(Family.lastname)
print("=" * 50)
# ================================================================================================
a = Family()
a.lastname = "박"    # 새로운 인스턴스 변수 생성
print(a.lastname)
print(Family.lastname)
print("=" * 50)
# ================================================================================================
Family.lastname = "박"       # Family의 클래스 변수인 lastname 값 자체가 변경
print(a.lastname)
print(Family.lastname)
b = Family()
print(b.lastname)