def fibonacci(n):

    if n == 0:
        return 0
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c

    return c


if __name__ =='__main__':
   x= fibonacci(6)
   print(x)