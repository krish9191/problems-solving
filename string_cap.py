def str_cap():
    str_1 = "good work done"
    str_2 = str_1.split()
    result = ''
    for item in str_2:
        # for j in list(item) :
        temp = item[0].upper() + item[1:]
        result = result + " " +temp

    print(result)


str_cap()
