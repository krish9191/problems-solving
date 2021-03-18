if __name__ == '__main__':

    arr = []
    arr_1 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    for j in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i][1] <= arr[(i - 1)][1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    for k in range(1, len(arr)):
        if arr[k][1] != arr[k - 1][1]:
            arr_1.append(arr[k])
            break

    for i in range(1, len(arr)):
        if arr_1[0][1] == arr[i][1] and arr_1[0][0]!= arr[i][0]:
            arr_1.append(arr[i])
    for j in range(len(arr_1)):
        for i in range(1, len(arr_1)):
            if arr_1[i][0] <= arr_1[(i - 1)][0]:
                arr_1[i - 1], arr_1[i] = arr_1[i], arr_1[i - 1]
    for m in range(len(arr_1)):
        print(arr_1[m][0])
