import torch

w = torch.tensor([[5., 10.], [1., 2.]], requires_grad=True)

optimizer = torch.optim.SGD([w], lr=0.001)


def my_function(variable):
    return (variable + 7).log().log().prod()


def make_gradient_step(function, variable):
    function_result = function(variable)
    function_result.backward()
    optimizer.step()
    optimizer.zero_grad()


for _ in range(500):
    make_gradient_step(my_function, w)

print(w, '<- gradient')
