pi = "31415926535897932384"

numbers = map(int, pi)
non_zero = filter(lambda x: x != 0, numbers)
vychisl = map(lambda x: 1 / x, non_zero) 
result = sum(vychisl)

zeros = list(filter(lambda x: x == 0, map(int, pi)))
for n in zeros:
    print("0")

print(result)