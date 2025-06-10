"""
You have a histogram. Try to find the size of the largest rectangle that you can build from the histogram columns.
"""


def largest_histogram(histogram):
    count = 0
    for i in range(len(histogram)):
        for j in range(i + 1, len(histogram) + 1):
            res = histogram[i:j]
            count = max(count, min(res) * len(res))
    return count


print(largest_histogram([5]))  # 5
print(largest_histogram([5, 3]))  # 6
print(largest_histogram([1, 1, 4, 1]))  # 4
print(largest_histogram([1, 1, 3, 1]))  # 4
print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))  # 8
print(largest_histogram([3, 3, 3, 6]))
