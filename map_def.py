
def str_f(list):
    result = ''
    for item in list:

        temp = item[0]
        result = result +temp
        return result
l = ["rajesh", "krishna"]
l_first = map(str_f, l)

print(list(l_first))

#
# str_f()

