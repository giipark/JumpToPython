BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'

# 메타 문자
# . ^ $ * + ? { } [ ] \ | ( )
# ================================================================================================
# [] 문자

# [a-zA-Z] : 모든 알파벳
# [0-9] : 모든 숫자
# [^0-9] : 숫자가 아닌 문자 (^은 not)

# \d 은 [0-9]
# \D 는 [^0-9]
# \s 는 [ \t\n\r\f\v]
# \S 는 [^ \t\n\r\f\v]
# \w 는 [a-zA-Z0-9_]
# \W 는 [^a-zA-Z0-9_]
# 대문자는 소문자의 반대라고 생각할 수 있음
# ================================================================================================
# .(dot) 문자

# a.b 는 "a + 모든_문자 + b"
# aab 매치 O
# a0b 매치 O
# abc 매치 X - 'a'와 'b' 사이에 어떤 문자라도 하나는 있어야 함
# ================================================================================================
# * 문자

# ca*t  - 'a'가 0번 이상 반복되면 매치
# ct 매치 O
# cat 매치 O
# caaat 매치 O
# ================================================================================================
# + 문자

# ca+t 는 "c + a가_1번_이상_반복 + t"
# ct 매치 X   - 'a'가 반복되지 않음
# cat 매치 O
# caaat 매치 O
# ================================================================================================
# {} 문자

# {m,n} 은 반복 횟수가 m부터 n까지인 문자와 매치
# {3,} 은 3 이상 반복 매치
# {,3} 은 3 이하 반복 매치

# {1,} 은 + 과 동일
# {0,} 은 * 과 동일

# {m}
# ca{2}t    - "c + a를_반드시_2번_반복 + t"
# cat 매치 X  - 'a'가 1번만 반복되어 매치 X
# caat 매치 O

# {m,n}
# ca{2,5}t 는 "c + a를_2~5회_반복 + t"
# cat 매치 X  - 'a'가 1번만 반복되어 매치 X
# caat 매치 O
# caaaaat 매치 O
# ================================================================================================
# ? 문자

# ? 는 {0, 1}
# ab?c
# abc 매치 O
# ac 매치 O
# abbbc 매치 X    -  0개 또는 1개만 존재해야 함
# ================================================================================================
print(f"{BRIGHT_BLUE}match{RESET}")
import re

# 한 번 만든 패턴 객체를 여러 번 사용해야 할 경우 compile을 사용하는 것이 편리 (메모리 효율성 up)
pattern = re.compile('[a-z]+')

# 한 번에 compile 및 match 메서드를 같이 사용 가능 (재활용 하기 힘듬)
# m = re.match('[a-z]+', 'python')

m = pattern.match('python')
print(m)    # match
m = pattern.match('3 python')   # 문자 3 때문에 매치 X
print(m)    # None

m = pattern.match('string')
if m:
    print('Match found:', m.group())
else:
    print('No match')
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}search{RESET}")

m = pattern.search('python')    # <re.Match object; span=(0, 6), match='python'>
print(m)
m = pattern.search('3 python')  # <re.Match object; span=(2, 8), match='python'>
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}findall{RESET}")

result = pattern.findall("life is too short")
print(result)   # [a-z]+ 와 매치되는 모든 값을 찾아 list로 반환
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}finditer{RESET}")

result = pattern.finditer("life is too short")
print(result)   # <callable_iterator object at 0x000002AAAEB77F10>

for r in result:
    print(r)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}Method of match object{RESET}")

m = pattern.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = pattern.search('3 python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print("=" * 50)
# ================================================================================================
# compile options
print(f"{BRIGHT_BLUE}DOTALL, S{RESET}")

pattern = re.compile('a.b')
m = pattern.match('a\nb')
print(m)    # None

# '\n' 문자와도 매치되게 하고 싶을 경우
pattern = re.compile('a.b', re.DOTALL)
m = pattern.match('a\nb')
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}IGNORECASE, I{RESET}")

# 대소문자 구별 없이 매치를 수행하고 싶은 경우
pattern = re.compile('[a-z]+', re.I)
m = pattern.match('python')
print(m)
m = pattern.match('Python')
print(m)
m = pattern.match('PYTHON')
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}MULTILINE, M{RESET}")

# ^python : 'python' 문자열로 시작
# \s : 공백 (space, tab, newline) 1개 포함
# \w+ : [a-zA-Z0-9_]이 1개 이상 포함
pattern = re.compile('^python\s\w+')

data = """python one
life is too short
python two
you need python
python three"""

# 'python two', 'python three' 는 문자열 중간에 있어서 매칭 X
print(pattern.findall(data))    # 'python one'

# MULTILINE, M 옵션을 사용하여, ^를 각 line의 처음이라는 의미로 변경
pattern = re.compile('^python\s\w+', re.M)
print(pattern.findall(data))
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}VERBOSE, X{RESET}")

charref = re.compile(r'&#(0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
&#                  # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
  | [0-9]+          # Decimal form
  | x[0-9a-fA-F]+   # Hexadecimal form
)
;
""", re.VERBOSE)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}\\ (Backslash){RESET}")

# \section 은 [ \t\n\r\f\v]ection 과 동일한 의미
# '\' 자체를 문자로 인식하고 싶은 경우
pattern = re.compile('\\section')   # \section으로 인식 되어 [ \t\n\r\f\v]ection가 compile

# 방법 1
pattern = re.compile('\\\\seciton')

# 방법 2 - raw string 사용
pattern = re.compile(r'\\section')
