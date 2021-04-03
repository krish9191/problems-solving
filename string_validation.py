if __name__ == '__main__':
    s = 'qA2'
    # print(any(char.isalnum for char in s))
    # print(any(char.isalpha for char in s))
    # print(any(char.isdigit for char in s))
    # print(any(char.islower for char in s))
    # print(any(char.isupper for char in s))
    #
    lf = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for item in lf:
        print(any(item(c) for c in s))
