def f(x):
    if x == 0 or x == 1:
        return 1
    a_0 = 1
    a_1 = 1
    for i in range(2, x + 1):
        a_i = a_0 + a_1 / (2 ** (i - 1))
        a_0, a_1 = a_1, a_i
    return a_1

x = 5
print(f(x))
