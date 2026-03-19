def f(x):
    if not isinstance(x, list):
        return str(x)
    if len(x) == 0:
        return ""
    return f(x[0]) + f(x[1:])
l0 = [1, 2, 3, 4, 5]
l1 = [[1, 2], [3, [[4]], 5]]
print(f(l0))
print(f(l1))
