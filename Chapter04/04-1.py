def add(a, b):
    return a + b


print(add(3, 4))


def say():
    return 'Hi'


a = say()
print(a)


def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


add(3, 4)


def sub(a, b):
    return a - b


result = sub(b=5, a=3)
print(result)
print(sub(7, 3))
print("=" * 50)


# ================================================================================================


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("=" * 50)


# ================================================================================================


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


print(add_mul("add", 1, 2, 3, 4, 5))
print(add_mul("mul", 1, 2, 3, 4, 5))
print("=" * 50)


# ================================================================================================


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name='foo', age=3)
print("=" * 50)


# ================================================================================================


def add_and_mul(a, b):
    return a + b, a * b


print(add_and_mul(3, 4))

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)
print("=" * 50)


# ================================================================================================


def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)


say_nick("바보")
say_nick("볼레")
print("=" * 50)


# ================================================================================================
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("홍길동", 32)
say_myself("김지원", 28, False)
print("=" * 50)
# ================================================================================================
a = 1


def vartest(a):
    a = a + 1


vartest(a)
print(a)
print("=" * 50)

# def vartest(a):
#     a = a + 1
#
# vartest(3)
# print(a)   - 오류발생: NameError: name 'a' is not defined
# ================================================================================================
a = 1


def vartest(a):
    a = a + 1
    return a


a = vartest(a)
print(a)

e = 1


def vartest():  # 되도록 global 명령어는 피하기
    global e
    e = e + 1


vartest()
print(e)
print("=" * 50)
# ================================================================================================
add = lambda a, b: a + b
result = add(3,4)
print(result)
