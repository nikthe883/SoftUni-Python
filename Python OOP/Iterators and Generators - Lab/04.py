def squares(n):
    i = 1
    while i <= n:
        yield i * i
        i += 1