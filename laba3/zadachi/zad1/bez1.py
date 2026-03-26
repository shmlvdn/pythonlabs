def f(x):
    result = []
    stack = [x]
    while stack:
        element = stack.pop()
        if type(element) == list:
            for n in reversed(element):
                stack.append(n)
        else:
            result.append(str(element))
    return ' -> '.join(result) + ' -> None'

print(f([1, [2, [3, [4, [5]]]]]))
