def chck_substr():
    x = 'all is well'
    sub_str = 'is'
    temp = ''
    for i in x:
        for j in sub_str:
            if j == i:
                temp = temp + j
    if temp == sub_str:
        print('true')

    else:
        print('false')


chck_substr()
