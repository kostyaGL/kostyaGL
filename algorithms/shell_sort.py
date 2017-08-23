def shell_sort(lst):
    sub_list_count = len(lst) // 2
    while sub_list_count > 0:

        for start_position in range(sub_list_count):
            gap_insertion_sort(lst, start_position, sub_list_count)

        sub_list_count //= 2
    return lst


def gap_insertion_sort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):

        current_value = lst[i]
        position = i

        while position >= gap and lst[position - gap] > current_value:
            lst[position] = lst[position - gap]
            position -= gap

        lst[position] = current_value


print(shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
