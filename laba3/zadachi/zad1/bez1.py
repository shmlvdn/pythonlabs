def f(x: list) -> str:
    if not list:
        return ""
    result = ""
    for a in x: 
        if isinstance(a, list): result = result + f(a)
        else: result += str(a)
    return result
l0 = [1, 2, 3, 4, 5]
l1 = [1, 2], [3, [[ 4 ]], 5]
print(f(l0))
print(f(l1))
