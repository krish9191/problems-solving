import functools


def mul_deco2(func):
    @functools.wraps(func)
    def display_1():
        print('I am rajesh')

    display_1()


def mul_deco(func):
    @functools.wraps(func)
    def display_2():
        print("What's your name?")

    display_2()


def mul_deco1(func):
    @functools.wraps(func)
    def display(*para1, **para2):
        return func(*para1, **para2)

    return display()


@mul_deco2
@mul_deco
@mul_deco1
def greet(name='krishna'):
    print(f'Hello, i am {name}')
