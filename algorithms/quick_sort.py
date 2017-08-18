def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x > pivot:
                greater.append(x)
            elif x == pivot:
                equal.append(x)
            elif x < pivot:
                less.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


print(quick_sort([5, 4, 3, 2, 1]))