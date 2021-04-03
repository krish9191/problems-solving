import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string,max_width))
# if __name__ == '__main__':
#     string, max_width = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4
#     result = wrap(string, max_width)
#
# def wrap(string, max_width):
#     s = ""
#     for c in range(0,len(string),max_width):
#         s += string[c:c+max_width] + "\n"
#     return s
if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4
    result = wrap(string, max_width)

    print(result)