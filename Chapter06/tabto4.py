import sys

if len(sys.argv) < 3:
    print("오류: python tabto4.py [원본 파일] [변환 파일]")
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

try:
    with open(src, 'r', encoding='utf-8') as f:
        data = f.read()

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(data.replace('\t', ' ' * 4))
except FileNotFoundError:
    print("원본 파일이 존재하지 않습니다.")
