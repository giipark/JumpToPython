dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)
print(dic['phone'])

a = {1: "hi"}
print(a)

a = {'a': [1, 2, 3]}
print(a)

a = {1: 'a'}
a[2] = 'b'
a['name'] = 'pey'
print(a)

del a[1]  # del a[key] - {Key:Value}쌍 삭제
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])
a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

a = {1: 'a', 1: 'b'}
print(a[1])  # Key가 중복일 경우, 마지막으로 저장한 Value가 출력

# a = {[1,2] : 'hi'}    - 오류발생: TypeError: unhashable type: 'list'

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a)
print(a.keys())  # dict_keys(['name', 'phone', 'birth'])
print(a.values())  # dict_values(['pey', '010-9999-1234', '1118'])
print(a.items())  # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

for k in a.keys():
    print(k)

print(list(a.keys()))

a.clear()
print(a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('nokey'))  # 출력값: None
# print(a['nokey'])         - 오류발생: KeyError: 'nokey'

print(a.get('nokey', 'foo'))
print(a.get('nokey'))

print('name' in a)
print('email' in a)

if 'name' in a:
    print("name = " + a.get('name'))
elif 'nokey' in a:
    print("nokey = " + a.get('nokey'))
else:
    print("NO")