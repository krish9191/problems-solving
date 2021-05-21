n = int(input('enter number of methods you used:'))
work_list = [1, 3, 44, 85, 54]

for i in range(n):
    u_input, *args = input().split()
    arg = list(map(int, args))
    if u_input == 'insert' and len(arg) == 2:
        work_list.insert(arg[0], arg[1])

    elif u_input == 'append' and len(arg) == 1:
        work_list.append(arg[0])

    elif u_input == 'remove' and len(arg) == 1:
        work_list.remove(arg[0])
    elif u_input == 'print':
        print(work_list)
    elif u_input == 'sort':

        work_list.sort()

    elif u_input == 'pop' and len(arg) == 1:

        work_list.pop(arg[0])
    elif u_input == 'reverse':

        work_list.reverse()
