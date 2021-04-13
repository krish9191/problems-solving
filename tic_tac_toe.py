def matrix_transpose(arr):
    arr_t = [[8 for i in range(len(arr))] for j in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr_t[j][i] = arr[i][j]
    return arr_t


if __name__ == '__main__':
    N = int(input('enter the no.of square matrix:'))
    tac=[[8 for i in range(N)]for j in range(N)]
    tac_d1=[]
    tac_d2=[]
    for i in range(N):
        for j in range(N):
            b, c,a = map(int, input().split())
            tac[b][c]=a
            for i in range(N):
                for j in range(N - 1, -1, -1):
                    if i == b and j == c and b + c == N-1:
                        tac_d2.append(a)
            if len(tac_d2) == N and sum(tac_d2) == 0:
                print('0 win the game')
            elif len(tac_d2) == N and sum(tac_d2) == N:
                print('1 win the game')
            if b == c:
                tac_d1.append(a)
            if len(tac_d1) == N and sum(tac_d1) == 0:
                print('0 win the game')
            elif len(tac_d1) == N and sum(tac_d1) == N:
                print('1 win the game')
            tac_t = matrix_transpose(tac)
        # [[tac[j][i] for j in range(len(tac))] for i in range(len(tac[0]))]
            for item in range(N):
                if sum(tac[item])==0:
                    print('0 win the game')
                elif sum(tac[item])==N:
                    print('1 win the game')
                elif sum(tac_t[item])==N:
                    print('1 win the game')
                elif sum(tac_t[item])==0:
                    print(f'0 win the game')
    print('it is a draw game')







