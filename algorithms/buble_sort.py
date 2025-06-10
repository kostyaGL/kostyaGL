def bubble(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubble([3, 2, 1]))
