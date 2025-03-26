import numpy as np

arr1 = np.random.rand(2, 3)
arr2 = np.random.rand(2)

# print(arr1 * arr2)  # 오류발생 - ValueError: operands could not be broadcast together with shapes (2,3) (2,)

arr2 = arr2[:, None]
print(arr2.shape)
res = arr1 * arr2
print(res.shape)
print(res)
print("=" * 50)
# ================================================================================================
arr1 = np.random.rand(2, 1, 3, 1)
arr2 = np.random.rand(1, 4, 1, 5)

print((arr1 + arr2).shape)
print("=" * 50)
# ================================================================================================
arr1 = np.random.rand(4, 1, 2, 3)
arr2 = np.random.rand(1, 5, 3, 4)

print((arr1 @ arr2).shape)

"""
특정 차원들의 shape이 같아야 동작하는 연산들을 많이 봤습니다.
하지만 특정한 조건을 만족하는 경우, 꼭 shape이 같지 않아도 연산들이 수행되는 경우가 있는데,
이러한 기작을 broadcasting이라고 부름
"""