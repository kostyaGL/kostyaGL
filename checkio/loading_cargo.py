# You are given a list of how to weigh objects to be loaded.
# You must distribute them all so that the difference between Total weight in each hand was as short as possible.

# Dynamic programming:
#   list of stones = [3,3,10,3]
#                                     left hand   |  right hand
#  operationN operation               ----------    ----------
#     1          sum of stones           19              0
#     2          19 >=(3+0)              19          0, 3
#     3          19 >=(3+3)              19          0, 3, 6
#     4          19 >=(3+6)              19          0, 3, 9
#     5          19 >=(3+9)              19          0, 3, 9
#
#           sum(list of stones) - 2 * max([0, 3, 9]) (e.g: 19- 18: res 1)
#


def checkio(data):
    sumdata, outputs = sum(data), {0}  # sum of all elements in left hand, right hand set with 0
    for n in data:
        outputs |= {m + n for m in outputs if m + n <= sumdata // 2}
    return sumdata - 2 * max(outputs)


print(checkio([10, 10]))
print(checkio([10]))
print(checkio([5, 8, 13, 27, 14]))
print(checkio([5, 5, 6, 5]))
print(checkio([12, 30, 30, 32, 42, 49]))
print(checkio([1, 1, 1, 3]))
