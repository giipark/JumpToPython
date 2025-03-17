import time


def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print(f"함수 수행 시간: {end - start} 초")
        return result
    return wrapper

@elapsed
def myfunc():
    for _ in range(10000):
        print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()

myfunc()

"""
Python Decorator
- 함수를 감싸서 '기능을 동적으로 추가'하는 함수
- 함수를 인자로 받아서 새로운 함수를 반환
- logging, 권한 검사, 실행시간측정, 함수 수정 등

Java Annotaion
- '메타데이터'를 추가하여 컴파일러나 프레임워크가 특정 동작을 수행하도록 도움 (참고역할)
- 클래스, 메서드, 필드 등에 추가되어 컴파일러나 런타임에서 특정 동작 수행
- DI, 런타임 설정, 컴파일 경고, 프레임워크 설정(Spring 등)
"""