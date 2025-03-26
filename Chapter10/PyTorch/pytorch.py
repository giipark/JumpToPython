import torch
import numpy as np

tensor = torch.tensor([1, 2, 3, 4])
print(tensor)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3, 4)
tensor = torch.tensor(arr)
print(tensor)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3, 4)
tensor = torch.tensor(arr)
print(arr.shape, tensor.shape)
print("=" * 50)
# ================================================================================================
tensor1 = torch.tensor(np.random.randn(3, 1, 5))
tensor2 = torch.tensor(np.random.randn(3, 4, 1))

print((tensor1 + tensor2).shape)
print((tensor1 - tensor2).shape)
print((tensor1 * tensor2).shape)
print((tensor1 / tensor2).shape)