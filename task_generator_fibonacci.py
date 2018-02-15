def fibonacci(n):
    x1=0
    x2=1
    while n != 0:
        x1, x2 = x2, x1+x2
        yield x1
        



