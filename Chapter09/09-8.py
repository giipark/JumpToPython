"""
딕셔너리
주어진 딕셔너리에서 value가 30인 key를 출력하세요.

sample_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
"""

sample_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
for key, value in sample_dict.items():
    if value == 30:
        print(key)