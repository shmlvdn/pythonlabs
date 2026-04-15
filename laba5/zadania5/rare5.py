def pi_generator():
    pi_digits = "31415926535897932384"
    for digit in pi_digits:
        yield int(digit)

digits = list(pi_generator())
non_zero = filter(lambda x: x != 0, digits)
vychisl = map(lambda x: 1 / x, non_zero)
result = sum(vychisl)

print(result)
