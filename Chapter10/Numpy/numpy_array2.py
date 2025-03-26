import numpy as np

arr = np.arange(6)

print(arr)
# 최댓값, 최솟값, 합, 평균, 표준편차
print(arr.max(), arr.min(), arr.sum(), arr.mean(), arr.std())
print("=" * 50)
# ================================================================================================
arr = np.arange(6).reshape((2, 3))
print(arr)
print(arr.max(), arr.min(), arr.sum(), arr.mean(), arr.std())
print("=" * 50)
# ================================================================================================
arr = np.arange(6).reshape((2, 3))
print(arr, "\n")
print(arr.max(axis=0))
print(arr.min(axis=0))
print(arr.sum(axis=0))
print(arr.mean(axis=0))
print(arr.std(axis=0))
print("=" * 50)
# ================================================================================================
arr = np.array([1, 2, 3, 4, 5, 6, 1, 2, 1, 5, 6])
print(np.unique(arr))
uniq_vals, uniq_cnts = np.unique(arr, return_counts=True)
print(uniq_vals)
print(uniq_cnts)
print("=" * 50)
# ================================================================================================
arr = np.random.randint(0, 10, size=(2, 3))
print(arr)
print(np.sort(arr, axis=1))
print("=" * 50)
# ================================================================================================
arr = np.random.randint(0, 10, size=6)
index = np.argsort(arr)
print(arr)
print(index)
print(arr[index])
print("=" * 50)
# ================================================================================================
arr = np.random.randn(2, 3, 4)
arr1 = np.split(arr, 2, axis=-1)

for arr in arr1:
    print(arr.shape)
print("=" * 50)
# ================================================================================================
arr2 = np.split(arr, [2, 3], axis=-1)

for arr in arr2:
    print(arr.shape)
print("=" * 50)
# ================================================================================================
arr1 = np.array([[1, 1, 1], [2, 2, 2]])
arr2 = np.array([[3, 3, 3], [4, 4, 4]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print("=" * 50)
# ================================================================================================
arr1 = np.random.rand(2, 3)
arr2 = np.random.rand(3, 4)

print((arr1 @ arr2).shape)
print(np.matmul(arr1, arr2).shape)
print("=" * 50)
# ================================================================================================
arr1 = np.random.rand(10, 2, 3)
arr2 = np.random.rand(10, 3, 4)

print((arr1 @ arr2).shape)
print("=" * 50)
# ================================================================================================
arr1 = np.random.rand(2, 5, 2, 3)
arr2 = np.random.rand(2, 5, 3, 4)

print(arr1)
print((arr1 @ arr2).shape)