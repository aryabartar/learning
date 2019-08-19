def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_rec(n - 2) + fib_rec(n - 1)


mem_dict = {}


def fib_mem(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    p1 = mem_dict.get(n - 2)
    if p1 is None:
        p1 = fib_mem(n - 2)
        mem_dict[n - 2] = p1

    p2 = mem_dict.get(n - 1)
    if p2 is None:
        p2 = fib_mem(n - 1)
        mem_dict[n - 1] = p2

    return p1 + p2


def fib_iter(n):
    a = 0
    b = 1

    for i in range(0, n - 1):
        b = a + b
        a = b - a
    return b


print(fib_iter(20))
