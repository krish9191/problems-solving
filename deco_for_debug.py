import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
make_greeting("Benjamin")
# 1.Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
# 2.Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r specifier means that repr() is used to represent the value.
# 3.The lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
# 4.The return value is printed after the function is executed.