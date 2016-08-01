# DIGING CANAL
# Algorithm heap

import heapq

ORTHOGONAL = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def checkio(data):
    """
    Return the count of cells to be excavated to connect the top and bottom.
    data: An array of arrays.  One is land, zero is water.
    """
    height, width = len(data), len(data[0])

    # The open list stores (number excavated, x, y) tuples.
    open_list = [(0, x, -1) for x in range(width)]
    visited = set()
    while open_list:
        # Explore one of the least dug cells
        dist, x, y = heapq.heappop(open_list)
        # If we've made it to the top, we're done.  Return dist.
        if y == height - 1:
            return dist
        visited.add((x, y))
        # Explore all adjacent cells
        for dx, dy in ORTHOGONAL:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    # If there is dirt, add one to dist.
                    node = (dist + data[ny][nx], nx, ny)
                    heapq.heappush(open_list, node)
