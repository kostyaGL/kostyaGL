def merge_sort(data):
    if len(data) == 1:
        return data

    res, med = [], len(data) // 2
    x, y = merge_sort(data[:med]), merge_sort(data[med:])

    while len(x) and len(y):
        if x[0] > y[0]:
            res.append(y.pop(0))
        else:
            res.append(x.pop(0))
    res.extend(x + y)
    return res


print(merge_sort([5, 4, 3, 2, 1]))
