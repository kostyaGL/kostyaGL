def insertion_sort(data):
    for i in range(1, len(data)):
        position = i
        current_value = data[i]
        while position and data[position - 1] > current_value:
            data[position] = data[position - 1]
            position -= 1
        data[position] = current_value
    return data


print(insertion_sort([6, 5, 4, 3, 2, 1]))
