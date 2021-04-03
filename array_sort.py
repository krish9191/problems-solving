def array_sort():
    arr_1 = [45, 5,60, 85, 54,17,15 ]

    for i in range(len(arr_1)):
        for j in range(1,len(arr_1)):
            if arr_1[j] <= arr_1[j - 1]:
                arr_1[j], arr_1[j - 1] = arr_1[j - 1], arr_1[j]

    print(arr_1)


array_sort()
