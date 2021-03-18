def maxV_array():


    n = 5
    arr = [2, 3, 6, 6, 5]
    max = arr[0]

    for j in range(1, n):
        if arr[j] >= max:
            max, arr[j] = arr[j], max
    arr.remove(max)

    for i in arr:
        if i==(len(arr)-1):
            print(arr[i])
maxV_array()