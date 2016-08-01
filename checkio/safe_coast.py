# SAFE COAST

from heapq import heappop, heapify, heappush

PERM = [(k, v) for k in range(-1, 2) for v in range(-1, 2) if not (k, v) == (0, 0)]


def finish_map(data):
    mappa = [list(i) for i in data]
    height, width = len(mappa), len(mappa[0])
    heap = [(i, y) for i in range(height) for y in range(width) if mappa[i][y] == 'X']
    heapify(heap)
    find_insecure(heap, width, height, mappa)
    points = [(i, y) for i in range(height) for y in range(width) if mappa[i][y] == 'D']
    heapify(points)
    find_secure(points, width, height, mappa)
    for _, value in enumerate(mappa):
        for key, val in enumerate(value):
            if value[key] == ".":
                value[key] = "S"

    return ["".join(j) for j in mappa]


def find_insecure(heap, width, height, mappa):
    while heap:
        x_cord, y_cord = heappop(heap)
        for x, y in PERM:
            dx = x_cord + x
            dy = y_cord + y
            if height > dx >= 0 and width > dy >= 0:
                if not mappa[dx][dy] == "X":
                    mappa[dx][dy] = "S"
    return mappa


def find_secure(points, width, height, mappa):
    visited = set()
    while points:
        x_cord, y_cord = heappop(points)
        rows = find_rows(x_cord, y_cord, height, width)
        for row, col in rows:
            if (row, col) in visited:
                continue
            if mappa[row][col] == "S" or mappa[row][col] == "." or mappa[row][col] == "D":
                if mappa[row][col] == "S":
                    continue
            visited.add((row, col))
            mappa[row][col] = "D"
            heappush(points, (row, col))
    return mappa


def find_rows(x_cor, y_cord, height, width):
    path = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ret = []
    for x, y in path:
        dx = x_cor + x
        dy = y_cord + y
        if 0 <= dx < height and 0 <= dy < width:
            ret.append((dx, dy))
    return ret


print finish_map(("D..XX.....",
                  "...X......",
                  ".......X..",
                  ".......X..",
                  "...X...X..",
                  "...XXXXX..",
                  "X.........",
                  "..X.......",
                  "..........",
                  "D...X....D"))
