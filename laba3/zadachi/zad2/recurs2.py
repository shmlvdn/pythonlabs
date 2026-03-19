def f(x):
    if x == 0 or x == 1:
        return 1
    return f(x - 2) + f(x - 1) / (2**(x - 1))
x = 4
print(f(x))