def string_count(string):
    split_string = string.split(' ')
    str_count = {}
    for item in split_string:
        if item in str_count.keys():
            str_count[item] = str_count[item] + 1
        else:
            str_count[item] = 1
    return str_count


print(string_count("i am who i am"))
