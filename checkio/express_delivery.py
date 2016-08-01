# EXPRESS DELIVERY:

def stringization(grid):
    return tuple(map(tuple, grid))


def count_boxes(path):
    if path.count("B") % 2:
        return 1
    return 2


def min_path(data, points, with_b=True):
    move = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
    start = points[0]
    end = points[1]
    queue = [(0, data, start, "")]
    while queue:
        (cost, data, positions, path) = queue.pop(0)
        if with_b:
            if end == positions and path.count("B") == 2:
                return (cost + 2, path)
        elif not with_b:
            if end == positions and not path.count("B"):
                return (cost, path)
        for direction, cord in move.iteritems():
            dx = positions[0] + cord[0]
            dy = positions[1] + cord[1]
            if 0 <= dx < len(data) and 0 <= dy < len(data) and "W" not in data[dx][dy]:
                grid = [list(i) for i in data]

                if grid[dx][dy] == "B":
                    grid[positions[0]][positions[1]], grid[dx][dy] = grid[dx][dy], grid[positions[0]][positions[1]]
                    deliver_time = count_boxes(path + direction + "B")
                    queue.append((cost + deliver_time, grid, (dx, dy), path + direction + "B"))
                grid[positions[0]][positions[1]], grid[dx][dy] = grid[dx][dy], grid[positions[0]][positions[1]]
                deliver_time = count_boxes(path + direction)
                queue.append((cost + deliver_time, grid, (dx, dy), path + direction))


def checkio(data):
    start_point = [(row_ind, col_ind) for row_ind, row in enumerate(data)
                   for col_ind, col in enumerate(row)
                   if col == "S" or col == "E"]
    time_with_load_cargo, path_with_load = min_path(data, start_point)
    time_with_no_load, path_with__no_load = min_path(data, start_point, False)
    print time_with_load_cargo, path_with_load, time_with_no_load, path_with__no_load
    if time_with_load_cargo < time_with_no_load:
        return path_with_load
    return path_with__no_load


print checkio(["S...",
               "....",
               "B.WB",
               "..WE"])
print checkio(["S...",
               " ....",
               "B..B",
               "..WE"])
