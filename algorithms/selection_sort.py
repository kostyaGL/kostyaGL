def selection_sort(lst):
    for fill_slot in reversed(range(len(lst))):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location

        temp = lst[fill_slot]
        lst[fill_slot] = lst[position_of_max]
        lst[position_of_max] = temp
    return lst

print(selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
