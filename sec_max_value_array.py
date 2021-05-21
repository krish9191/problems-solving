arr = map(int, input().split(','))
new_arr = list(set(arr))
for item in new_arr:
    for j in range(1, len(new_arr)):
        if new_arr[j - 1] >= new_arr[j]:
            new_arr[j - 1], new_arr[j] = new_arr[j], new_arr[j - 1]

print(new_arr[len(new_arr) - 2])
