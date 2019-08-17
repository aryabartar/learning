def sum_func(n):
    # Base case
    if n < 10:
        return n

    # Recursion
    else:
        return n % 10 + sum_func(n / 10)


print(sum_func(4321))
