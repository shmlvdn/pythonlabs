def limit_calls(n=None):
    def decorator(func):
        count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal count
            if n is not None and count >= n:
                print("Лимит вызовов исчерпан!")
                return None
            count += 1
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@limit_calls(3)
def hello(name):
    return f"Привет, {name}!"


@limit_calls()
def hello2(name):
    return f"Привет, {name}!"


def recursive_sum(n):
    # Рекурсивно вычисляет сумму чисел от 1 до n
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)


print("С ограничением")
print(hello("Диана"))   
print(hello("Ксюша"))   
print(hello("Юлия"))   
print(hello("Игорь"))   

print("\nБез ограничения")
print(hello2("Диана"))   
print(hello2("Ксюша"))   
print(hello2("Юлия"))   
print(hello2("Игорь"))   

print("\nРекурсивная функция:")
print("Сумма чисел от 1 до 5:", recursive_sum(5))
print("Сумма чисел от 1 до 10:", recursive_sum(10))