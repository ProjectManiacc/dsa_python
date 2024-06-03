def fibo_gen(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def fibo_iter(num):
    a, b = 0, 1
    while num > 0:
        a, b = b, a + b
        num -= 1
    return a


def fibo_rec(num):
    if num <= 1:
        return 1
    return fibo_rec(num - 1) + fibo_rec(num - 2)


print(f"\nfibo_iter")
for n in range(10):
    print(fibo_iter(n))

print(f"\nfibo_gen")
for n in fibo_gen(10):
    print(n)

print(f"\nfibo_rec")
for n in range(10):
    print(fibo_rec(n))



