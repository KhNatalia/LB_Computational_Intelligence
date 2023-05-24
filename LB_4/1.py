import torch

my_torch = torch.tensor(list(range(9)))
first_point = my_torch[1]

print("Створений тензор: ", my_torch)
print("Розмір:", my_torch.size())
print("Зсув:", my_torch.storage_offset())
print("Крок:", my_torch.stride())
