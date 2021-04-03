import functools


def mul_deco2(func):
    @functools.wraps(func)
    def display_1():
        print('deco2')
        print('hello, i am rajesh')
    display_1()
def mul_deco(func):

    def display_2():
        print('deco')
        print('lets introduce ourselves')
    display_2()
def mul_deco1(func):
    def display(*para1,**para2):
        print('deco 1')
        return func(*para1,**para2)
    return display()


@mul_deco2
@mul_deco
@mul_deco1
def greet(name='krishna'):
    print(f'hello i am {name}')


