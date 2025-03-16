def add(a, b):
    return a + b


def sub(a, b):
    return a - b

# 직접 파일을 실행했을 때는 main으로 읽어 참이므로 실행o
# 모듈을 import 해서 사용할 경우에는 main이 아니므로 거짓으로 실행x
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

"""
🔥__name__ 변수란?
파이썬이 내부적으로 사용하는 특별한 변수 이름

* 직접 파일을 실행할 경우, __name__ 변수에 __main__ 값이 저장
* 다른 파이썬 모듈에서 import할 경우에는 __name__ 변수에 모듈 이름인 mod1이 저장
"""