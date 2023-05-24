import torch

b = torch.arange(1, 10)
b = b.view(3, 3)
print("Старий:\n", b)

b = b[1:, 1:]
print("Новий:\n", b)
