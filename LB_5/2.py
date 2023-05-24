import torch

w = torch.tensor([[5., 10.], [1., 2.]], requires_grad=True)
alpha = 0.001

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
w = w.to(device)

for _ in range(500):
    # it's critical to calculate function inside the loop:
    function = (w + 7).log().log().prod()
    function.backward()

    w.data -= alpha * w.grad
    w.grad.zero_()

print(w, '<- gradient')
