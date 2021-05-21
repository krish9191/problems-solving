if __name__ == '__main__':
    s = 'AABcc'

    lf = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for item in lf:
        print(any(item(c) for c in s))
