BRIGHT_BLUE = '\033[94m'
RESET = '\033[0m'

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# ndim - 차원
# size - arr의 전체 원소의 개수
# shape - 각 차원을 따라 몇 개의 원소가 있는지
print(arr.ndim, arr.size, arr.shape)
print("=" * 50)
# ================================================================================================
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print(arr_2d.ndim, arr_2d.size, arr_2d.shape)
print("=" * 50)
# ================================================================================================
arr_float = np.array([1., 2, 3, 4, 5])
print(arr_float.dtype, arr_float.dtype)
print("=" * 50)
# ================================================================================================
arr_float2 = np.array([1, 2, 3, 4, 5], dtype=float)
print(arr_float2.shape)
print(arr_float2.dtype)
print("=" * 50)
# ================================================================================================
zeros = np.zeros(5)
print(zeros)
print(zeros.shape)
print("=" * 50)
# ================================================================================================
zeros_nd = np.zeros((32, 32, 3))
print(zeros_nd)
print(zeros_nd.shape)
print("=" * 50)
# ================================================================================================
ones = np.ones((2, 3))
print(ones)
print("=" * 50)
# ================================================================================================
range1 = np.arange(5)
range2 = np.arange(0, 5)
range3 = np.arange(0, 5, step=1)
range4 = np.arange(0, 10, 0.5)

print(range1)
print(range2)
print(range3)
print(range4)
print("=" * 50)
# ================================================================================================
range1 = np.linspace(0, 4, 5)
range2 = np.linspace(0, 9.5, 20)
range3 = np.linspace(0, 10, 4)

print(range1)
print(range2)
print(range3)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3, 4)  # not tuple!!
print(arr)
print("=" * 50)
# ================================================================================================
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.shape)

arr1 = np.reshape(arr, (2, 3))
arr2 = arr.reshape((3, 2))
print(arr1.shape, arr2.shape)
print(arr1)
print(arr2)
print("=" * 50)
# ================================================================================================
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

arr = arr.reshape(6)
print(arr.shape)
print(arr)
print("=" * 50)
# ================================================================================================
arr = np.array([1, 2, 3, 4, 5, 6])
# arr.reshape((2, 2))  # 오류발생 - ValueError: cannot reshape array of size 6 into shape (2,2)
arr = arr.reshape((2, 3))
print(arr)
print("=" * 50)
# ================================================================================================
arr = np.zeros((3, 4, 5))  # 3차원 배열 - 각 4행 5열
print(arr.shape)
print(arr)

arr1 = arr.reshape((3, -1))  # 4 * 5 = 20 이 합쳐짐 / 2차원 배열 - 3행 20열
arr2 = arr.reshape((-1, 5))  # 3 * 4 = 12 이 합쳐짐 / 2차원 배열 - 12행 5열
print(arr1.shape, arr2.shape)
print(arr1)
print(arr2)
print("=" * 50)
# ================================================================================================
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

arr1 = arr[:, np.newaxis]
arr2 = arr[:, None]
arr3 = np.expand_dims(arr, axis=1)  # No arr.expand_dims!!

print(arr1.shape, arr2.shape, arr3.shape)
print(arr1)
print("=" * 50)
# ================================================================================================
arr1 = arr[None]
arr2 = arr[:, None]
arr3 = arr[:, :, None]
arr4 = arr[..., None]

print(arr1.shape, arr2.shape, arr3.shape, arr4.shape)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print("=" * 50)
# ================================================================================================
arr1 = np.zeros(3)
arr2 = np.zeros(1)
arr3 = np.zeros(4)

arr = np.concatenate([arr1, arr2, arr3])
print(arr.shape)
print(arr)
print("=" * 50)
# ================================================================================================
arr1 = np.zeros((2, 3, 5))
arr2 = np.zeros((2, 1, 5))
arr3 = np.zeros((2, 4, 5))

arr = np.concatenate([arr1, arr2, arr3], axis=1)
print(arr.shape)
print("=" * 50)
# ================================================================================================
arr1 = np.zeros((2, 3))
arr2 = np.zeros((2, 3))
arr3 = np.zeros((2, 3))

arr4 = np.stack([arr1, arr2, arr3], axis=0)
arr5 = np.stack([arr1, arr2, arr3], axis=-1)
print(arr4.shape, arr5.shape)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3, 4)
print(arr.shape)
print(arr)

arr = arr.transpose([1, 0, 2])
print(arr.shape)
print(arr)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3, 4)

# https://stackoverflow.com/questions/28930465/what-is-the-difference-between-flatten-and-ravel-functions-in-numpy
arr1 = arr.flatten()  # arr의 값을 copy하여 arr1에 저장
arr2 = arr.ravel()  # arr의 1차원 배열을 반환
arr3 = arr.reshape(-1)  # arr의 데이터 변경 없이 형상만 변경하여 반환

print(arr1.shape, arr2.shape, arr3.shape)
print("=" * 50)
# ================================================================================================
print(f"{BRIGHT_BLUE}Indexing{RESET}")
arr = np.array([1, 2, 3, 4, 5, 6])

print(arr[1], arr[-1], arr[-3])
print(arr[:5], arr[1:5], arr[2:-2])
print("=" * 50)
# ================================================================================================
arr = np.arange(1, 25, 1).reshape((2, 3, 4))
print(arr.shape)

print(arr[0, 0, 0], arr[1, 0, -1])
print(arr[1, 2, :].shape, arr[1, :, 2].shape, arr[:, 1, 2].shape)
print(arr[1, :, :].shape, arr[:, 2, :].shape, arr[:, :, -2].shape)
print(arr[1, 2].shape, arr[:, 2].shape, arr[..., -2].shape)
