"""
예외 처리
"""

# FileNotFoundError: [Errno 2] No such file or directory: 'File that does not exist'
# f = open("File that does not exist", 'r')

# ZeroDivisionError: division by zero
# print(4 / 0)

a = [1, 2, 3]
# IndexError: list index out of range
# a[3]
"""
try:
    f = open("File that does not exist", 'r')
except FileNotFoundError as e:
    print(e)
finally:
    f.close()   # NameError: name 'f' is not defined
"""
try:
    with open("File that does not exist", 'r') as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)

try:
    print(a[3])
    print(4 / 0)
except (ZeroDivisionError, IndexError) as e:
    print(e)
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
print("=" * 50)
# ================================================================================================
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
