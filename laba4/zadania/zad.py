def limit_calls(max_calls):
    count = 0
    def decorator(func):
        def wrapper(*args):
            nonlocal count
            count += 1
            if count <= max_calls:
                return func(*args)
            return None
        return wrapper
    return decorator


def unique():
    a = set()
    
    def f(*args):
        spisok = []
        for x in args:
            if x not in a:
                a.add(x)
                spisok.append(x)
        return spisok
    return f


u = unique()
limited_unique = limit_calls(3)(u)

print(limited_unique(1, 2, 2, 3, 4))
print(limited_unique(2, 3, 4, 4, 10, 10))  
print(limited_unique(5, 6, 7))            
