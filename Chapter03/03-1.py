money = True
if money:
    print("택시를 타고 가라")
else:
    # print("걸어 가라")    - 오류발생: IndentationError: unexpected indent
    print("걸어 가라")

x = 3
y = 2
print(x > y)  # True
print(x < y)  # False
print(x <= y)  # False
print(x >= y)  # True
print(x != y)  # True
print("=" * 50)

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
print("=" * 50)

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('j' not in 'python')
print("=" * 50)

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', ('money', 5000)]
money = next((amt for x in pocket if isinstance(x, tuple) and x[0] == 'money' for amt in [x[1]]), 0)
if 'money' in [x[0] if isinstance(x, tuple) else x for x in pocket] and money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print("=" * 50)

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
print("=" * 50)

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print("=" * 50)

score = 30
message = "success" if score >= 60 else "failure"
print(message)
