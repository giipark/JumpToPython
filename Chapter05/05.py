from Tools.scripts.summarize_stats import emit_pair_counts

print("연습문제")
print("=" * 50)
# ================================================================================================
questtion = """아래와 같은 클래스 Person을 생성하세요:

클래스 속성: name, age
생성자: __init__(self, name, age): name과 age를 인자로 받아 객체를 초기화합니다.
메소드: greet(self): "{name}님이 {age}살입니다" 형식의 문자열을 반환합니다.
예시 코드를 작성하고 테스트해보세요.
"""
print(f"Q1. {questtion}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"{self.name}님이 {self.age}살입니다."


person1 = Person("홍길동", 30)
print(person1.greet())  # 출력: 홍길동님이 30살입니다.
print("=" * 50)
# ================================================================================================
question = """아래와 같은 클래스 BankAccount을 생성하세요:

클래스 속성: account_number, balance
생성자: __init__(self, account_number, balance=0): account_number와 초기 잔액 balance(기본값 0)을 인자로 받아 객체를 초기화합니다.
메소드: deposit(self, amount): 계좌에 amount만큼 입금합니다.
메소드: withdraw(self, amount): 계좌에서 amount만큼 출금합니다. 잔액이 출금액보다 작을 경우 "잔액이 부족합니다"라고 출력합니다.
예시 코드를 작성하고 테스트해보세요.
"""
print(f"Q2. {question}")


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount


account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다.
print("=" * 50)
# ================================================================================================
question = """아래와 같은 간단한 모듈 calculator.py를 작성하고, 다른 파이썬 스크립트에서 이 모듈을 사용해보세요.

함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
함수: multiply(a, b): 두 숫자의 곱을 반환합니다.
함수: divide(a, b): 두 숫자의 나눗셈 결과를 반환합니다. 0으로 나누는 경우, "0으로 나눌 수 없습니다"라고 출력합니다.
예시 코드를 작성하고 테스트해보세요.
"""
print(f"Q3. {question}")
import calculator

print(calculator.add(3, 4))  # 출력: 7
print(calculator.substract(3, 4))  # 출력: -1
print(calculator.multiply(3, 4))  # 출력: 12
print(calculator.divide(3, 0))  # 출력: 0으로 나눌 수 없습니다.
print(calculator.divide(3, 4))  # 출력: 0.75
print("=" * 50)
# ================================================================================================
question = """파이썬 표준 라이브러리 random 모듈을 사용하여 1부터 100 사이의 무작위 정수를 10개 생성하고, 이를 오름차순으로 정렬하는 코드를 작성하세요.

예시 코드를 작성하고 테스트해보세요.
"""
print(f"Q4. {question}")
import random

num_list = []
for _ in range(10):
    num = random.randint(1, 100)
    num_list.append(num)

print(sorted(num_list))
print("=" * 50)
# ================================================================================================
question = """아래와 같은 간단한 패키지 my_math를 생성하세요.

패키지: my_math
모듈: operations.py
함수: add(a, b): 두 숫자의 합을 반환합니다.
함수: subtract(a, b): 두 숫자의 차를 반환합니다.
패키지를 생성한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요.
"""
print(f"Q5. {question}")
from my_math.operations import add, substract

print(add(3, 4))
print(substract(3, 4))
print("=" * 50)
# ================================================================================================
question = """위의 my_math 패키지에 다음과 같이 새로운 모듈 geometry.py를 추가하세요.

모듈: geometry.py
함수: circle_area(radius): 원의 반지름을 입력받아 넓이를 반환합니다. (넓이 = 반지름 x 반지름 x π)
함수: rectangle_area(width, height): 사각형의 가로와 세로를 입력받아 넓이를 반환합니다. (넓이 = 가로 x 세로)
패키지를 수정한 후, 다른 파이썬 스크립트에서 이 패키지를 사용해보세요.

예시 코드를 작성하고 테스트해보세요."""
print(f"Q6. {question}")
from my_math.geometry import circle_area, rectangle_area

print(circle_area(5))
print(rectangle_area(4, 5))
print("=" * 50)
# ================================================================================================
question = """아래 코드는 사용자로부터 숫자를 입력받아 제곱을 출력하는 코드입니다. 
사용자가 숫자가 아닌 문자를 입력할 경우, ValueError 예외가 발생할 수 있습니다.
이 예외를 처리하고, 사용자에게 숫자를 입력하도록 안내하는 코드를 작성하세요."""
print(f"Q7. {question}")

number = input("숫자를 입력하세요: ")
try:
    squared_number = int(number) ** 2
except ValueError:
    print("정확한 숫자를 입력해주세요.")
else:
    print("입력한 숫자의 제곱:", squared_number)
print("=" * 50)
# ================================================================================================
question = """아래 코드는 두 숫자를 나누는 코드입니다. 분모가 0인 경우, ZeroDivisionError 예외가 발생할 수 있습니다.
이 예외를 처리하고, 사용자에게 0으로 나눌 수 없다는 메시지를 출력하는 코드를 작성하세요."""
print(f"Q8. {question}")

numerator = 10
denominator = 0
try:
    result = numerator / denominator
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("결과:", result)
print("=" * 50)
# ================================================================================================
question = """다음과 같은 리스트가 주어졌을 때, max()와 min() 내장 함수를 사용하여 최댓값과 최솟값을 찾고 출력하는 코드를 작성하세요."""
print(f"Q9. {question}")

numbers = [3, 7, 2, 1, 6, 4, 9, 8]
print("numbers 리스트의 최댓값:", max(numbers))
print("numbers 리스트의 최솟값:", min(numbers))
print("=" * 50)
# ================================================================================================
question = """주어진 문자열에서 공백을 기준으로 단어를 분리하고, 각 단어의 첫 글자를 대문자로 변경한 후, 다시 공백을 기준으로 합쳐서 출력하는 코드를 작성하세요.
이 문제를 해결하기 위해 str.split(), str.capitalize(), str.join() 내장 함수를 사용하세요."""
print(f"Q10. {question}")

text = "hello world, this is a python example."
text_list = text.split(" ")
capitalized_list = []
for t in text_list:
    capitalized_list.append(t.capitalize())
print(" ".join(capitalized_list))
print("=" * 50)
# ================================================================================================
question = """파이썬 datetime 모듈을 사용하여 현재 시간을 출력하는 코드를 작성하세요."""
print(f"Q11. {question}")
import datetime

now = datetime.datetime.now()
print("현재 시간:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("=" * 50)
# ================================================================================================
question = """파이썬 random 모듈을 사용하여 1에서 100 사이의 무작위 정수 10개를 생성하고 출력하는 코드를 작성하세요."""
print(f"Q12. {question}")
import random

random_list = [random.randint(1, 100) for _ in range(10)]
print("무작위 정수 10개:", random_list)