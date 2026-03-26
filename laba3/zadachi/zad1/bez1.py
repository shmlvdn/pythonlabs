def f(x: list) -> str:
    if not x:
        return ""
    
    result = ""
    stack = list(x)
    
    while stack:
        element = stack.pop()
        
        if isinstance(element, list):
            stack.extend(reversed(element))
        else:
            result = str(element) + result
    return result

l0 = [1, 2, 3, 4, 5]
l1 = [1, [2], [3, [[4]]], 5]

print(f(l0)) 
print(f(l1))
