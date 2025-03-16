from copy import copy, deepcopy

a = 1
b = 1
print(id(a), id(b))
print(id(a) == id(b))
b = a
a = 2
print(b)
print(id(a) == id(b))
print("=" * 50)

"""
Python에서는 변수가 값을 직접 저장하지 않고, 객체(값)의 참조(Reference)만 저장
a라는 변수는 1이라는 객체를 가리키는 "이름표" 역할을 할 뿐
"""

"""
Python에서 메모리는 크게 Stack과 Heap으로 나뉘어 관리.

🔹 1️⃣ Stack 영역 (변수 이름 저장)
- 지역 변수(변수명, 참조) 가 저장되는 공간.
- 실제 데이터(값)는 저장되지 않고, Heap 영역의 객체를 가리키는 참조(Reference) 가 저장됨.
- 함수 호출 시 새로운 Stack 프레임이 생성됨.

🔹 2️⃣ Heap 영역 (객체 저장)
- 모든 객체(값) 가 저장되는 공간.
- int, str, list, dict 같은 Python의 모든 객체가 Heap에 저장됨.
- Garbage Collector(GC)가 사용되지 않는 객체를 자동으로 정리함.

a = 1
b = a

Stack                     Heap
──────────────────        ─────────────
a ────────────▶  1 (int) │ (이미 존재)
b ────────────▶  (같은 1을 참조)
──────────────────        ─────────────

Python의 "이름(name) 바인딩" 방식
- 변수는 변수끼리 연결되는 게 아니라, 값(객체)과 연결됨
- 따라서, a = 2로 바뀌어도 b는 여전히 1을 참조.
- b가 a의 주소를 참조하고 있는 것이 아님.

Python의 변수 = 값을 직접 저장하는 게 아니라, 객체를 가리키는 이름표
"""

"""
JAVA
int a = 10;
int b = a;  // 값이 복사됨 (Stack에 저장됨)
a = 20;
System.out.println(a);  // 20
System.out.println(b);  // 10 (b는 영향을 받지 않음)

- Java에서는 int 같은 Primitive Type은 값이 Stack에 직접 저장되므로, b는 a의 영향을 받지 않음!
- 즉, Java는 값이 복사되지만, Python은 a, b가 같은 객체를 참조하는 방식
"""

a = 1
b = 'python'
c = [1, 2, 3]

print(id(a))  # 객체의 메모리 주소 - 140736688943912
print(type(a))  # 객체의 Type - <class 'int'>
print(a)  # 값 - 1

print(id(c))
print(id(c[0]))
print(id(c[1]))
print(id(c[2]))

print(id(a) == id(c[0]))  # heap에 저장된 int(1)의 메모리 주소
print("=" * 50)

a = [1, 2, 3]
b = a
print(a is b)

# 리스트(list) 같은 가변 객체(Mutable Object)는 변수 간에 공유
a[1] = 4
print("a =", a)
print("b =", b)
print(a is b)  # True
print("=" * 50)

b = a[:]  # a.copy(), copy(a) 동일
a[1] = 5
print("a =", a)
print("b =", b)
print(a is b)  # False
print("=" * 50)

b = a.copy()
a[1] = 6
print("a =", a)
print("b =", b)
print(a is b)  # False
print("=" * 50)

a = [1, [2, 3]]
b = copy(a)  # 새로운 리스트를 만들지만, 내부 요소는 기존 리스트의 요소를 참조
a[1][0] = 4  # 내부 리스트(list안의 list)는 공유됨 - 얕은 복사(Shallow Copy)
print("a =", a)
print("b =", b)
print(a is b)  # False - is는 변수의 Object(객체)가 같을때 True 리턴
print(a == b)  # True - ==는 변수의 Value(값)이 같을때 True 리턴
print(a[1] is b[1])  # True
print("=" * 50)

b = deepcopy(a)  # 내부 리스트까지 완전히 새로운 객체로 복사
a[1][0] = 6
print("a =", a)
print("b =", b)  # 내부 리스트의 값이 변경되지 않음 - 깊은 복사(Deep Copy)
print("=" * 50)

a, b = ('python', 'life')
print(a)
print(b)
[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)
print("=" * 50)

a = 3
b = 5
print("a =", a)
print("b =", b)
a, b = b, a
print("a =", a)
print("b =", b)


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a, b = swap(a, b)
print("a =", a)
print("b =", b)
