def f(x):
    result = []

    def l(n):
        if type(n) == list:
            for element in n:
                l(element)
        else:
            result.append(str(n))
    l(x)
    return ' -> '.join(result) + ' -> None'

print(f([1, [2, [3, [4, [5]]]]]))
