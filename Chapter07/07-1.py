#최초의 문자 셋, ASCII
# ASCII는 7bit, 128개

# 유니코드, Unicode
# 비영어권 국가에서 자신의 문자를 표현하고자 하는 요구가 생김
# 서유럽 문자 셋 - ISO8859
# 한국 문자 셋 - KSC5601

a = "Life is too short"
b = a.encode('utf-8')
print(b)
print(type(b))
print("=" * 50)
# ================================================================================================

a = "한글"
# a.encode('ascii') - 오류발생: UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
b = a.encode('euc-kr')
print(b)
print(type(b))
# c = b.decode('utf-8') - 오류발생: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte
c = b.decode('euc-kr')
print(c)
print(type(c))
print("=" * 50)
# ================================================================================================
b = a.encode('utf-8')
print(b)
print(type(b))
c = b.decode('utf-8')
print(c)
print(type(c))
# ================================================================================================
# 파이썬 소스 코드의 인코딩을 명시하기 (파이썬 3.0부터는 기본: utf-8)
# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-