def limit_calls(max_calls):
    count = 0
    
    def decorator(func):
        def wrapper(*args):
            nonlocal count
            count += 1
            if count <= max_calls:
                return func(*args)
            else:
                return None
        return wrapper
    return decorator
@limit_calls(4)
def say_hello():
    print("Привет!")

say_hello()
say_hello()
say_hello()
say_hello()  
say_hello()  
