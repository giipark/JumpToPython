import sys

option = sys.argv[1]

if option in ['-w', '-a']:
    if len(sys.argv) < 3:
        print("오류: 메모 내용을 입력해주세요.")
        sys.exit(1)
    memo = sys.argv[2] + '\n'

    mode = 'w' if option == '-w' else 'a'
    with open('memo.txt', mode, encoding='utf-8') as f:
        f.write(memo)
elif option == '-v':
    try:
        with open('memo.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("메모 파일이 존재하지 않습니다.")
else:
    print("오류: 올바른 옵션을 입력해주세요. (-w, -a, -v)")
