print("연습문제")
print("=" * 50)
# ================================================================================================
print("Q1. 주어진 문자열을 반대로 뒤집는 함수 reverse_string을 작성하세요. 예를 들어, 입력 문자열이 ""Python""이면 출력은 ""nohtyP""이어야 합니다.")


def reverse_string(s):
    return s[::-1]


input_str = "Python"
output_str = reverse_string(input_str)
print(output_str)

print(input_str[1::-1])  # 1번째 부터 역순으로 출력
print(input_str[1:4:-1])  # 1번째 부터 역순으로 4번까지 (범위, 방향이 맞지않아 출력X) 빈문자열
print("=" * 50)
# ================================================================================================
print(
    "Q2. 주어진 숫자가 소수인지 아닌지를 판별하는 함수 is_prime을 작성하세요. 소수는 1과 자기 자신만을 약수로 갖는 1보다 큰 양의 정수입니다. 함수는 소수일 경우 True를 반환하고, 아닐 경우 False를 반환해야 합니다.")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    print(f"{num}은 소수인가? {is_prime(num)}")
print("=" * 50)
# ================================================================================================
print("Q3. 사용자로부터 숫자를 입력받아 그 숫자의 제곱 값을 출력하는 프로그램을 작성하세요.")
num = int(input("숫자를 입력해주세요: "))
print(f"{num}의 제곲 값: {num ** 2}")
print("=" * 50)
# ================================================================================================
print("Q4. 사용자로부터 이름과 나이를 입력받아, 10년 후의 나이를 출력하는 프로그램을 작성하세요.")
name = input("이름을 입력해주세요: ")
age = int(input("숫자를 입력해주세요: "))
print(f"10년 후의 나이는 {age + 10}살 입니다.")
print("=" * 50)
# ================================================================================================
print("Q5. 사용자로부터 입력받은 내용을 파일에 작성하는 프로그램을 작성하세요. 파일 이름은 ""input.txt""로 합니다.")
input_str = input("내용을 입력해주세요: ")
with open("input.txt", 'w', encoding="utf-8") as f:
    f.write(input_str)
print("입력한 내용이 input.txt 파일에 저장되었습니다.")
print("=" * 50)
# ================================================================================================
print("Q6. 파일에 있는 모든 줄을 읽어 대문자로 변환하여 출력하는 프로그램을 작성하세요. 파일 이름은 ""example.txt""로 합니다.")
with open("example.txt", 'r', encoding="utf-8") as f:
    # Solution 1
    # lines = f.readlines()
    # for line in lines:
    #     print(line.upper().strip())

    # Solution 2
    # for line in f:
    #     print(line.upper().strip())

    # Solution 3
    data = f.read()
print(data.upper())
print("=" * 50)
# ================================================================================================
print("Q7. 명령 줄 인수로 두 숫자와 사칙연산 기호(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.")
# calculator.py
