print('datetime')
import datetime

now = datetime.datetime.now()
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2025, 3, 15)
diff = day2 - day1
print(diff.days)
print(now)
print(day2.weekday())
print(day2.isoweekday())
print("=" * 50)
# ================================================================================================
print('time')
import time

print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x', time.localtime()))
print(time.strftime('%c', time.localtime()))
print(time.strftime('%Z', time.localtime()))
for i in range(10):
    print(i)
    # time.sleep(1)
print("=" * 50)
# ================================================================================================
print("math")
import math

print(math.gcd(6, 12, 18))
print(math.lcm(6, 11))
print("=" * 50)
# ================================================================================================
import random

print(random.random())
print(random.randint(1, 100))


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
print("=" * 50)


# ================================================================================================
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
print("=" * 50)
# ================================================================================================
data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data)))
print("=" * 50)
# ================================================================================================
print('itertools')
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))
print("=" * 50)
# ================================================================================================
print("permutation")
p = itertools.permutations([1, 2, 3], 2)
result = list(p)
print(result)
print(len(result))
print("=" * 50)
# ================================================================================================
print("combination")
it = itertools.combinations([1, 2, 3], 2)
result = list(it)
print(result)
print(len(result))
# print(len(list(itertools.combinations_with_replacement(range(1, 46), 6))))  # 중복허용
print("=" * 50)
# ================================================================================================
print("functools")
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)
print("=" * 50)
# ================================================================================================
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
min_num = functools.reduce(lambda x, y: x if x < y else y, num_list)
print(max_num)
print(min_num)
print("=" * 50)
# ================================================================================================
print("operator.itemgetter")
from operator import itemgetter, attrgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))  # itemgetter(튜플 요소의 인덱스 번호)
print(result)
print("=" * 50)
# ================================================================================================
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)
print("=" * 50)


# ================================================================================================
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Studnet(name={self.name}, age={self.age}, grade={self.grade}"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.grade}"


students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('age'))
print(result)
for r in result:
    print(r)
print("=" * 50)
# ================================================================================================
print('shutil')
import shutil
import os

shutil.copy('C:/Users/rlgus/Documents/workspace/JumpToPython/Chapter04/example.txt', 'example.txt.bak')

if os.path.exists('C:/Users/rlgus/Documents/workspace/JumpToPython/Chapter04/example.txt.bak'):
    os.remove('C:/Users/rlgus/Documents/workspace/JumpToPython/Chapter04/example.txt.bak')
shutil.move('example.txt.bak', 'C:/Users/rlgus/Documents/workspace/JumpToPython/Chapter04')
print("=" * 50)
# ================================================================================================
print("glob")
import glob

gb = glob.glob('../Chapter*/*.py')
for g in gb:
    print(g)
print("=" * 50)
# ================================================================================================
print("pickle")
import pickle

with open('test.txt', 'wb') as f:
    data = {1: 'python', 2: 'java', 3: 'c'}
    pickle.dump(data, f)

with open("test.txt", 'rb') as f:
    data = pickle.load(f)
print(data)
print("=" * 50)
# ================================================================================================
print('os')
import os

print(os.environ)
print(os.path)
print(os.name)
print(os.environ['PATH'])
original_dir = os.getcwd()
print(os.chdir('C:\\Users\\rlgus\\Documents\\workspace\\JumpToPython'))
print(os.getcwd())
print(os.system("dir"))
with os.popen("dir") as f:
    print(f.read())
os.chdir(original_dir)
print(os.getcwd())
print("=" * 50)
# ================================================================================================
print("zipfile")
import zipfile

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('test')
    myzip.write('test.bak')
    myzip.write('test.txt')

# 파일 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()

# 특정 파일만 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('test')

# 압축하여 묶기
with zipfile.ZipFile('mytext2.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    myzip.write('test')
    myzip.write('test.bak')
    myzip.write('test.txt')
print("=" * 50)
# ================================================================================================
print("threding")
# thread_test.py
print("=" * 50)
# ================================================================================================
import tempfile

filename = tempfile.mkstemp()
print(filename)

f = tempfile.TemporaryFile()
f.close()
print("=" * 50)
# ================================================================================================
print("traceback")
import traceback


def a():
    return 1 / 0


def b():
    a()


def main():
    try:
        b()
    except:
        print("오류 발생!!")
        print(traceback.format_exc())


main()
print("=" * 50)
# ================================================================================================
print("json")
import json

with open('myinfo.json', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))
print(data)

data = {'name': '김이박', 'birth': '0330', 'age': 34}
with open('myinfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

d = {"name": "홍길동", "birth": "0525", "age": 30}
json_data = json.dumps(d)
print(json_data)
print(json.loads(json_data))
json_data = json.dumps(d, indent=2,
                       ensure_ascii=False)
print(json_data)
print(json.dumps([1, 2, 3]))
print(json.dumps((4, 5, 6)))
print("=" * 50)
# ================================================================================================
print("urllib")
import urllib.request

# SSL 인증서 검증을 비활성화하는 Context 생성
import ssl
context = ssl._create_unverified_context()

def get_wikidocs(page):
    resource = f'https://wikidocs.net/{page}'
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())

get_wikidocs(33)
print("=" * 50)
# ================================================================================================
print("webbrowser")
import webbrowser

webbrowser.open_new('http://python.org')
webbrowser.open('http://python.org')