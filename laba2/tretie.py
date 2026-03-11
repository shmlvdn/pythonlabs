def f():
    a = []
    n = 452022
    
    while len(a) < 5:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                M = i + n // i
                if M % 7 == 3:
                    a.append((n, M))
                break
        n += 1
        
    print(a)


f()
