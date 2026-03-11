def f():
    x = 16 ** 18 * 4 ** 10 - 46 - 16
    k = 0
    while x > 0:
        if x % 4 == 3:
            k += 1
        x = x // 4
    print(k)
    
f()