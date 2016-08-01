def checkio(grid):
    perform = res(grid)
    return perform


def res(grid, x=0, y=0):
    for i in range(x, len(grid)):
        for j in range(y, len(grid)):
            if grid[i][j] == 0:
                a = set(range(1, 10))
                for k in range(9):
                    a -= {grid[k][j], grid[i][k], grid[(i - i % 3) + k // 3][(j - j % 3) + k % 3]}
                if not a:
                    return
                for k in a:
                    grid[i][j] = k
                    if res(grid, x, y): return grid
                grid[i][j] = 0
                return
    return grid


print checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
               [0, 0, 1, 0, 3, 0, 5, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 8, 5, 9, 7, 2, 6, 4, 0],
               [0, 0, 0, 6, 0, 1, 0, 0, 0],
               [0, 2, 6, 3, 8, 5, 9, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 3, 0, 5, 0, 2, 0, 0],
               [8, 0, 0, 4, 9, 7, 0, 0, 6]])
