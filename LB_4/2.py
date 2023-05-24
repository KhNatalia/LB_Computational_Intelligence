import torch

b = torch.arange(1, 10)
b = b.view(3, 3)

print(b)
print("b[1][1]: ", b[1, 1])
