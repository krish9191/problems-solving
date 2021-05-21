import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


enter_string, width = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4
result = wrap(enter_string, width)
print(result)
