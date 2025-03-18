# 정규식(regular expression)

datas = [
    ('park', '800905-1049118'),
    ('kim', '700905-1059119')
]

result = [(name, ssn[:8] + '*' * (len(ssn) - 8)) for name, ssn in datas]
print(result)
print("=" * 50)
# ================================================================================================

import re

# 정규표현식을 미리 컴파일
pattern = re.compile(r'(\d{6}-\d)\d{6}')

# 1번 방식
masked_datas = []
for name, ssn in datas:
    masked_ssn = pattern.sub(r'\1******', ssn)  # 한 자리 숫자 그룹 참조
    masked_datas.append((name, masked_ssn))
print(masked_datas)

# 2번 방식
masked_datas = []
for name, ssn in datas:
    masked_ssn = pattern.sub('\g<1>******', ssn)    # 여러 자리 숫자 그룹 참조
    masked_datas.append((name, masked_ssn))
print(masked_datas)

# 3번 방식
pattern = re.compile(r'(\d{6}-\d)\d{6}')
masked_datas = [(name, pattern.sub(r'\1******', ssn)) for name, ssn in datas]
print(masked_datas)