# 8 puzzle
# https://py.checkio.org/en/mission/8-puzzle/


def tuplization(data):
    return tuple(tuple(col for col in row) for row in data)


def match(data, start):
    pattern = range(1, 9) + [0]
    positions = {(0, 1): "R", (1, 0): "D", (-1, 0): "U", (0, -1): "L"}
    queque = [(0, start, data, "")]
    seen = set()
    while queque:
        (cost, position, data, res) = queque.pop(0)
        seen.add(tuplization(data))
        if sum(data, []) == pattern:
            return cost, res

        for cord, pos in positions.iteritems():
            dx = cord[0] + position[0]
            dy = cord[1] + position[1]

            if 0 <= dx < 3 and 0 <= dy < 3:
                grid = [list(i) for i in data]
                grid[position[0]][position[1]], grid[dx][dy] = grid[dx][dy], grid[position[0]][position[1]]
                if tuplization(grid) not in seen:
                    queque.append((cost + 1, (dx, dy), grid, res + pos))


def checkio(data):
    find_min = [(i, y) for i in range(len(data)) for y in range(len(data)) if not data[i][y]][0]
    return match(data, find_min)[-1]


print checkio([[1, 2, 3],
               [4, 6, 8],
               [7, 5, 0]])
print checkio([[2, 4, 3],
               [1, 8, 5],
               [7, 6, 0]])
