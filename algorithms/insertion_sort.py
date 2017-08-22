def insertion_sort(lst):
    for index in range(1, len(lst)):

        current_value = lst[index]
        position = index

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position = position - 1

        lst[position] = current_value
    return lst


print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
