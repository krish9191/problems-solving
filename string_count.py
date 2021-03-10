def string_count():
    string1 = "i am who i am"

    string2 = string1.split(' ')

    str_count = {}
    for item in string2:
        if item in str_count.keys():
            str_count[item] = str_count[item] + 1
        else:
            str_count[item] = 1
    print(str_count)


string_count()
