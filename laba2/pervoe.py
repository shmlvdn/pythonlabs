from itertools import product

def f():
    k = 0
    for word in product("НАСТЯ", repeat=6):
        if word.count("А") <= 1 and word.count("Я") <= 1:
            k += 1
    print(k)


f()
