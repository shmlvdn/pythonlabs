def limit_calls(n):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= n:
                print("Лимит вызовов исчерпан!")
                return None
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Пример использования
@limit_calls(3)
def say_hello(name):
    return f"Привет, {name}!"

print(say_hello("Диана"))   
print(say_hello("Ксюша"))   
print(say_hello("Юлия"))   
print(say_hello("Игорь"))   