import torch
import numpy as np

arr = np.random.rand(2, 3)
tensor = torch.tensor(arr)

print(arr)
print(np.sum(arr, axis=-1))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(torch.sum(tensor, dim=-1))
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3)

tensor1 = torch.tensor(arr, device='cuda')
tensor2 = torch.tensor(arr)
tensor2 = tensor2.to('cuda')

print(tensor1.device, tensor2.device)
print(tensor1 + tensor2)
print("=" * 50)
# ================================================================================================
arr = np.random.rand(2, 3)

tensor1 = torch.tensor(arr, device='cuda')
tensor2 = torch.tensor(arr)

# print(tensor1 + tensor2)    # 오류발생 - RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!
