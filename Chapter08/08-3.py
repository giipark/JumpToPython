import re

BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'

print(f"{BRIGHT_BLUE}|{RESET}")

pattern = re.compile('Crow|Servo')
m = pattern.match('CrowHello')
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}^{RESET}")

print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}${RESET}")

print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}\\A{RESET}")
print("문자열의 처음과 매치된다는 것을 의미, ^와 동일")
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}\\Z{RESET}")
print("문자열의 끝과 매치된다는 것을 의미, $와 동일")
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}\\b{RESET}")  # word boundary

pattern = re.compile(r'\bclass\b')  # whitespace + 'class' + whitespace 인 것만 매치
print(pattern.search('no class at all'))
print(pattern.search('the declassified algorithm'))  # None
print(pattern.search('one subclass is'))  # None
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}\\B{RESET}")

pattern = re.compile(r'\Bclass\B')  # whitespace 가 1개라도 있는 경우에 매치 X
print(pattern.search('no class at all'))  # None
print(pattern.search('the declassified algorithm'))
print(pattern.search('one subclass is'))  # None
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}GROUPING{RESET}")

pattern = re.compile('(ABC)+')
m = pattern.search('ABCABCABC OK?')
print(m)

# \w+ : 문자 1개 이상
# \s+ : whitespace 1개 이상
# \d+ : 숫자 1개 이상
# - : '-' 문자
# \d+ : 숫자 1개 이상
# - : '-' 문자
# \d+ : 숫자 1개 이상
pattern = re.compile(r"\w+\s+\d+-\d+-\d+")  # '이름' + ' ' + '숫자-숫자-숫자'
m = pattern.search('park 010-1234-1234')
print(m)

pattern = re.compile(r"(\w+)\s+\d+-\d+-\d+")  # '이름' 부부만 그룹화하여 뽑아내기
m = pattern.search('park 010-1234-1234')
print(m)
print(m.group(1))  # ()로 그룹화된 값중 첫 번째 그룹 출력

pattern = re.compile(r"(\w+)\s+(\d+-\d+-\d+)")  # '이름', '전화번호' 부분 각각 그룹화
m = pattern.search('park 010-1234-1234')
print(m)
print(m.group(2))  # ()로 그룹화된 값중 두 번째 그룹 출력

pattern = re.compile(r"(\w+)\s+((\d+)-\d+-\d+)")  # '전화번호' 안에 그룹 중첩
m = pattern.search('park 010-1234-1234')
print(m)
print(m.group(3))  # 그룹 중첩시, 바깥쪽부터 시작해 안쪽으로 들어갈수록 그룹번호 증가
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}그루핑된 문자열 재참조하기 (\\1, \\2, ...){RESET}")

# 재참조 메타문자 '\1'
# 2개의 동일한 단어를 연속적으로 사용해야만 매치
pattern = re.compile(r'(\b\w+)\s+\1')
m = pattern.search('Paris in the the spring')
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}그루핑된 문자열에 이름 붙이기{RESET}")

# (?P<그룹명>...) - 그룹 이름 지정
pattern = re.compile(r"(?P<name>\w+)\s+((\d+)-\d+-\d+)")  # '이름' + ' ' + '숫자-숫자-숫자'
m = pattern.search('park 010-1234-1234')
print(m.group('name'))

# (?P=그룹이름) - 재참조 가능
pattern = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = pattern.search('Paris in the the spring').group()
print(m)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}긍정형 전방 탐색{RESET}")
# 긍정형 전방 탐색((?=...)): ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않음

pattern = re.compile(".+:")
m = pattern.search("https://google.com")
print(m.group())

pattern = re.compile(".+(?=:)")
m = pattern.search("https://google.com")
print(m.group())
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}부정형 전방 탐색{RESET}")
# 부정형 전방 탐색((?!...)): ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않음

# '.*[.].*$' 는 '파일_이름' + '.' + '확장자'

# '확장자가 bat인 파일은 제외해야 한다' 라는 조건 추가
# 1번 - '.*[.][^b].*$'
# 1번의 문제점은 bat이 아닌 모든 확장자가 제외 됨 (bar, bin, bzip)
# 2번 - '.*[.]([^b]..|.[^a].|..[^t])$'
# 2번은 첫 번째 문자가 b가 아니거나, 두 번째 문자가 a가 아니거나, 세 번재 문자가 t가 아닌 경우
# 2번의 문제점은 xxx.cf 같은 확장자의 문자 개수가 2개인 케이스가 제외가 됨
# 3번 - '.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$'

# 패턴이 너무 복잡함
# exe 파일도 제외가 필요해서 정규식을 추가한다면, 더욱 복잡해질 것임
pattern = re.compile('.*[.](?!bat$).*$')  # 확장자가 bat이 아닌 경우에만 통과
print(pattern.search('my.exe'))  # <re.Match object; span=(0, 6), match='my.exe'>
print(pattern.search('my.bat'))  # None

pattern = re.compile('.*[.](?!bat$|exe$).*$')
print(pattern.search('my.exe'))  # None
print(pattern.search('my.bat'))  # None
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}sub (문자열 바꾸기){RESET}")

pattern = re.compile('(blue|white|red)')
print(pattern.sub('colour', 'blue socks and red shoes'))
print(pattern.sub('colour', 'blue socks and red shoes', count=1))  # 바꾸기 횟수 제한

print(pattern.subn('colour', 'blue socks and red shoes'))  # subn은 기능은 동일하지만 'tuple'로 반환
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}sub 메서드 사용시 참조 구문 사용하기{RESET}")

pattern = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)-\d+-\d+)")
print(pattern.sub("\g<phone> \g<name>", 'park 010-1234-1234'))
print(pattern.sub("\g<2> \g<1>", 'park 010-1234-1234'))
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}sub 메서드의 매개변수로 함수 넣기{RESET}")


def hexrepl(match):
    value = int(match.group())
    return hex(value)


pattern = re.compile(r'\d+')
print(pattern.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}greedy와 non-greedy{RESET}")

s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())  # '<html>' 만 나오길 기대했지만, '<html><head><title>Title</title>' 출력

print(re.match('<.*?>', s).group())  # '<html> 만 출력

# non-greedy 문자인 '?' 사용법
# '*?', '+?', '??', '{m,n}?'
