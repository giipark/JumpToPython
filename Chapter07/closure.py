# Closure
# inner function을 구현하고 그 inner function을 반환하는 함수

# def mul3(n):
#     return n * 3
#
# def mul5(n):
#     return n * 5

# 위 코드는 비효율적인 코드
class Mul:
    def __init__(self, m):
        self.m = m

    # def mul(self, n):
    #     return self.m * n
    def __call__(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))
    print(mul5(10))