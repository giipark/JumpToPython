t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

t1 = (1, 2, 'a', 'b')
print(t1)
# del t1[1]     - 오류발생: TypeError: 'tuple' object doesn't support item deletion
# t1[1] = 3     - 오류발생: TypeError: 'tuple' object does not support item assignment

print(t1[2])
print(t1[1:])

t3 = t1 + t4
print(t3)

print(t1 * 3)
print(len(t1))

# AttributeError: 'tuple' object has no attribute
# t1.sort()
# t1.insert(1, 1)
# t1.remove(1)
# t1.pop()