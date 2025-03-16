odd = [1, 3, 5, 7, 9]
print(odd)

a = list()
print(a)
a = []
print(a)

b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(e[2][0])

e[1] = 3
e[2][0] = 'Death'
print(e)

e = 1, 2, ['Life', 'is']  # e = (1, 2, ['Life', 'is'])
# e[1] = 3  - 오류발생: TypeError: 'tuple' object does not support item assignment
print(e)

a = [1, 2, 3]  # 리스트(list)는 크기가 동적으로 변하는 배열
print(a[0])

a.append(4)  # Java의 ArrayList<T>와 비슷하게 동작
print(a)

a = [0] * 5
print(a)

a = [None] * 5
print(a)
a[2] = 3
print(a[0:3])

a = [1, 2, 3]
b = ["one", "two", "three"]
print(a)
print(b)
print(a + b)

print(b * 3)
print(len(b))
# print(a[2] + "hi")    - 오류발생: TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(a[2]) + "hi")

del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a.append(4)
a.append(5)
print(a)
a.append((6, 7))
print(a)
# a[4][0] = 1   - 오류발생: TypeError: 'tuple' object does not support item assignment

# a.sort()  - 오류발생: TypeError: '<' not supported between instances of 'tuple' and 'int'
del a[4]
a.sort()
a.append([3, 6])
# a.sort()  - 오류발생: TypeError: '<' not supported between instances of 'list' and 'int'
del a[4]
a.append(3)
print(a)
a.sort()
print(a)

a.reverse()
print(a)

a = ["one", "two", "three", "four", "five", "six"]
a.sort()  # sort는 사전 순으로 뒤집어버림
print(a)
a.reverse()  # reverse는 리스트의 순서를 단순하게 거꾸로 뒤집는 것
print(a)

print(a.index("one"))
# print(a.index(1))     - 오류발생: ValueError: 1 is not in list

a.insert(3, "seven")
print(a)

# a.remove(3)       - 오류발생: ValueError: list.remove(x): x not in list
a.remove("seven")
print(a)

a.pop()
print(a)

a.pop(1)
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a.pop()
a.extend([4, 5])
print(a)

b = [6, 7]
print(f"b = {b[0]}, {b[1]}")  # 가독성 최고
print("b = " + ", ".join(map(str, b)))  # 길이 변화에 유연
print("b = {0}, {1}".format(b[0], b[1]))  # 비교적 직관적
print("b =", *b, sep=",")  # 리스트 원소가 많을 때 유용
a.extend(b)
print(a)
print("a = " + ", ".join(map(str, a)))

a += [8, 9]
print(a)

a = a + [10, 11]
print(a)