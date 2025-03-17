import time

# *args는 모든 입력 인수를 tuple로 변환하는 매개변수
# **kwargs는 모든 '키=값' 형태의 입력 인수를 dictionary로 변환하는 매개변수

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print(f"함수 수행 시간: {end - start:.6f} 초")
        return result

    return wrapper


@elapsed
def myfunc(msg):
    print(f"'{msg}'를 출력합니다.")

@elapsed
def myfunc2(a, b, c):
    print(f"{a} * {b} * {c} = {a * b * c}")


# myfunc은 msg라는 인자가 1개 있는데,
# elapse.wrappers는 인자를 0개 받고 있으면, 아래와 같은 오류발생
# TypeError: elapsed.<locals>.wrapper() takes 0 positional arguments but 1 was given

myfunc('Python')
myfunc2(3, 4, 5)
