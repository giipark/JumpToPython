# from mod1 import add, sub     - 모듈 함수1, 모듈 함수2 사용
from mod1 import *
import mod2

print(add(4, 2))
print(sub(6, 3))
print("=" * 50)
# ================================================================================================
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(f"{mod2.add(mod2.PI, 4.4):.6f}")

"""
Java는 package를 사용하여 상위 폴더의 클래스를 가져올 수 있음
Python은 상위 디렉토리로 직접 import가 불가능

1️⃣sys.path를 이용한 방법
# c/c1.py
import sys
import os

sys.path.append(os.path.abspath("../b"))  # ✅ b 폴더를 import 가능하도록 설정
import b1  # ✅ 이제 b1.py를 import할 수 있음

b1.some_function()  # ✅ b1.py 내부의 함수를 사용할 수 있음
================================================================================================
2️⃣PYTHONPATH 환경 변수를 설정하는 방법

터미널에서 PYTHONPATH 추가
- export PYTHONPATH="../b:$PYTHONPATH"
- python c/c1.py

import b1  # ✅ 이제 바로 import 가능! 
================================================================================================
3️⃣__init__.py를 사용하여 패키지로 만들기
📂 a/
 ├── 📂 b/
 │   ├── __init__.py  # ✅ 패키지로 인식되도록 추가
 │   ├── b1.py
 ├── 📂 c/
 │   ├── c1.py
 
# c/c1.py
from b import b1  # ✅ 패키지처럼 import 가능!
"""