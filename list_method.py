if __name__ == '__main__':
    N = int(input())
    list_1 = []


    for i in range(N):
        a=input()
        u_input, *ind = a.split()
        arg = list(map(int, ind))
        if u_input =='insert' and len(arg)==2:
          list_1.insert(arg[0],arg[1])

        elif u_input == 'append' and len(arg)==1:
            list_1.append(arg[0])

        elif u_input == 'remove' and len(arg)==1:
            list_1.remove(arg[0])
        elif u_input == 'print':
            print(list_1)
        elif u_input == 'sort':
            list_1.sort()
        elif u_input == 'pop':
            list_1.pop()
        elif u_input == 'reverse':
            list_1.reverse()

