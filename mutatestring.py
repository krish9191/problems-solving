def mutate_string(string, position, character):
    s1 =list(string)

    s1[position]=character
    s2=''.join(s1)
    return s2

if __name__ == '__main__':
    s = input()
    i, c = input().split()

    s_new = mutate_string(s, int(i), c)

    print(s_new)
