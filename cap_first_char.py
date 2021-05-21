def str_cap(string):
    str_2 = string.split()
    result = ''
    for item in str_2:
        temp = item[0].upper() + item[1:]
        result = result + " " + temp
    return result


enter_string = 'michael john henry'
print(str_cap(enter_string))
