class FourCal:
    def __init__(self):
        self.first = None
        self.second = None

    def setdata(self, first, second):
        self.first = first
        self.second = second

    # @property     - a.add 처럼 () 없이 호출 가능
    # 정수(int) 속성처럼 동작 / () 붙이면, 정수(int)를 함수처럼 호출하려 한다 생각하여 오류발생
    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second


a = FourCal()
a.setdata(6, 3)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b = FourCal()
b.setdata(3, 8)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print("=" * 50)
# ================================================================================================
c1 = FourCal  # 클래스 자체를 변수에 할당 (객체 x)
c2 = FourCal()  # 클래스의 인스턴스를 생성 (객체 o)

print(c1)
# print(c2.add())   - 오류발생: TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

"""
Python은 Java에 비해 오류(예외)에 대해 훨씬 관대하고, 코드 실행을 최대한 중단하지 않으려고 함

Java
 - 타입 검사: 정적 타입 검사(Static Type Checking)
 - 예외 처리: 오류 발생 시 프로그램 중단(Exception)
 - 배열 범위 초과: ArrayIndexOutOfBoundsException 발생
 - null: NullPointerException(NPE) 발생

Python
 - 타입 검사: 동적 타입 검사(Dynamic Type Checking)
 - 예외 처리: try-except로 쉽게 예외 처리 가능
 - 배열 범위 초과: IndexError 발생, 예외 처리 가능
 - None: None은 if 문에서 안전하게 처리 가능
 
** Java의 try-catch도 예외처리 가능
** Java에서 예외 강제 처리(Checked Exception)는 반드시 예외 처리를 강제하는 특징이 있음
** Python에서 예외 처리(Unchecked Exception)는 강제되지 않음 (선택적)

** Java: throws / Python: raise
"""
print("=" * 50)


# ================================================================================================
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second


a = MoreFourCal()
a.setdata(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())
print("=" * 50)
# ================================================================================================