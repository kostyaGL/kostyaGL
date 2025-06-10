# Given a 2d grid map of 1 (land) and 0 (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#
# There was applied Depth-first search algorithm

PERM = [(i, y) for i in range(-1, 2) for y in range(-1, 2) if not (i, y) == (0, 0)]


def get_area(data, i, y):
    length = len(data)
    row_len = len(data[0])
    if i == length or i < 0:
        return 0
    if y == row_len or y < 0:
        return 0
    if not data[i][y]:
        return 0
    data[i][y] = 0
    gs = 1
    for c1, c2 in PERM:
        gs += get_area(data, i + c1, y + c2)
    return gs


def checkio(data):
    islands = []
    for key, row in enumerate(data):
        for key1, val in enumerate(row):
            if row[key1]:
                area = get_area(data, key, key1)
                islands.append(area)
    return islands


print(checkio([[0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0],
               [0, 0, 0, 1, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]))
