with open('euc_kr.txt', encoding='euc-kr') as f:
    data = f.read()

data = data + '\n' + '추가 문자열'
print(data)

# encoding='utf-8'로 지정하면, utf-8로 저장 할 수 있음
with open('euc_kr.txt', encoding='euc-kr', mode='w') as f:
    f.write(data)