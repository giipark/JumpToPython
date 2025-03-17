def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))
    print(mul5(10))

print(dir(mul3))
print(dir(mul3.__closure__))
print(mul3.__closure__)
print(type(mul3.__closure__))   # closure - tuple type
print(dir(mul3.__closure__[0]))
print(dir(mul3.__closure__[0].cell_contents))