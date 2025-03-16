f = open("새파일.txt", 'w')
f.close()
# ================================================================================================
f = open("C:/Users/rlgus/Documents/workspace/JumpToPython/Chapter04/새파일1.txt", 'w', encoding="utf-8")
f.write("새파일1")
f.close()
# ================================================================================================
f = open("새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# ================================================================================================
for i in range(1, 11):
    data = "%d번째 줄입니다." % i
    print(data)
print("=" * 50)
# ================================================================================================
#f = open("새파일.txt", 'r')   - 오류발생: UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 14: illegal multibyte sequence
f = open("새파일.txt", 'r', encoding="utf-8")  # utf-8 파일이므로 utf-8로 지정해줘야함
line = f.readline()
print(line)
f.close()
print("=" * 50)
# ================================================================================================
f = open("새파일.txt", 'r', encoding="utf-8")  # utf-8 파일이므로 utf-8로 지정해줘야함
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
print("=" * 50)
# ================================================================================================
f = open("새파일.txt", 'r', encoding="utf-8")  # utf-8 파일이므로 utf-8로 지정해줘야함
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
print("=" * 50)
# ================================================================================================
f = open("새파일.txt", 'r', encoding="utf-8")  # utf-8 파일이므로 utf-8로 지정해줘야함
data = f.read()
print(data)
f.close()
print("=" * 50)
# ================================================================================================
f = open("새파일.txt", 'a', encoding="utf-8")
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# ================================================================================================
with open("foo.txt", 'w', encoding="utf-8") as f:
    f.write("Life is too short, you need python")