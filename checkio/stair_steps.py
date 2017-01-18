# STAIR STEPS (Clear solution)
# There is a ladder with steps N and the two sites - one at the beginning and one at the end.
# At each step there is a number (from -100 to 100 except for 0).
# And the zeros are written sites. You are on the first floor and have to be in the second.
# To do this, you can step to the next step, or through one.
# You need to find a way that the sum of the numbers on the steps where you tread
# Was the maximum possible for this ladder.
# The result should be that amount.


def checkio(n):
    data = [0] + n + [0]
    for i in range(2, len(data)):
        data[i] += max(data[i - 1], data[i - 2])
    return data[-1]


print checkio([5, -3, -1, 2])
print checkio([5, 6, -10, -7, 4])
print checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])
print checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])
