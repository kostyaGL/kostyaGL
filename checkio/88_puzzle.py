"""
https://py.checkio.org/en/mission/88th-puzzle/
"""

G = (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)

R = ((0, 3, 5, 2), (1, 4, 6, 3), (5, 8, 10, 7), (6, 9, 11, 8))


def rotate(state, i):
    ret = list(state)
    ring = R[i]
    for k, v in enumerate(ring):
        ret[v] = state[ring[k - 1]]
    return ret


def puzzle88(state):
    q = list([(state, "")])

    while q:
        s, m = q.pop(0)

        if G == tuple(s):
            return m

        for i in range(4):
            q.append((rotate(s, i), m + str(i + 1)))


print(puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)))
print(puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)))
print(puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)))
