def level(r, c, l):
    result = set()
    for i in range(l):
        result.add((r - i, c - l + i))
        result.add((r + i, c + l - i))
        result.add((r - l + i, c + i))
        result.add((r + l - i, c - i))
    return result


def get_bacteria_size(grid, r, c):
    if not grid[r][c]:
        return
    l = 1
    while True:
        if all(grid[i][j] == 1 for i, j in level(r, c, l)):
            if all(grid[i][j] == 0 for i, j in level(r, c, l + 1)):
                return l
        else:
            return
        l += 1


def healthy(grid):
    grid = [[0] + list(row) + [0] for row in grid]
    grid.insert(0, [0] * len(grid[0]))
    grid.append([0] * len(grid[0]))
    max_size, max_center = 0, [0, 0]
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            size = get_bacteria_size(grid, r, c)
            if not size and size > max_size:
                max_size, max_center = size, [r - 1, c - 1]
    return max_center


print healthy(((0, 1, 0),
               (1, 1, 1),
               (0, 1, 0)))
