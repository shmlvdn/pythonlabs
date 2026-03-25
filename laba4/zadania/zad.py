# Декоратор, который просто выводит сообщение перед вызовом функции
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Вызывается функция...")
        result = func(*args, **kwargs)
        print("Функция завершила работу")
        return result
    return wrapper


def unique():
    a = set()
    
    @my_decorator
    def f(*args):
        spisok = []
        for x in args:
            if x not in a:
                a.add(x)
                spisok.append(x)
        return spisok
    return f


u = unique()
print(u(1, 2, 2, 3, 4))
print(u(2, 3, 4, 4, 10, 10))