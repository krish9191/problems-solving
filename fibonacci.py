def fibonacci(n):
    a = 0
    b = 1
    c = 0
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return c


x = fibonacci(4)
print(x)
