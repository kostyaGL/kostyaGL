import itertools
# https://py.checkio.org/en/mission/unfair-dice/

def winning_die(enemy_die):
    enemy_die_length = len(enemy_die)
    sum_enemy_die = sum(enemy_die)
    m = max(enemy_die)
    if m == 18:
        m += 1
    else:
        m += 2

    check = enemy_die_length % 2 == 1

    if check:
        rep = enemy_die_length // 2 + 1
    else:
        rep = enemy_die_length // 2
    for k in range(1, m):
        for i in itertools.product([k], range(1, m), repeat=rep):
            if check:
                res = i[:-1]
            else:
                res = i
            if (sum(res) == sum_enemy_die
                    and len(res) == enemy_die_length
                    and win(res, enemy_die)):
                return res
    return []


def win(player, enemy):
    return sum(1 if p > e else -1 if p < e else 0
               for p in player for e in enemy) > 0

print(winning_die([3, 3, 3, 3, 6, 6]))
print(winning_die([4, 4, 4, 4, 4, 4]))
print(winning_die([2, 2, 5, 5, 5, 5]))
print(winning_die([1, 1, 1, 4]))
print(winning_die([4, 4, 3]))
print(winning_die([5, 5, 5, 5, 5, 5]))
print(winning_die([6, 6, 6, 6, 6, 6]))
print(winning_die([1, 1, 1, 4]))
print(winning_die([3, 3, 3]))
print(winning_die([1, 1, 1]))
print(winning_die([1, 2, 3, 4, 5, 6]))
print(winning_die([2, 3, 4, 5, 6, 7]))
print(winning_die([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(winning_die([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(winning_die([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))
print(winning_die([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(winning_die([1, 5, 5, 5, 5, 6, 6, 6, 6, 10]))
print(winning_die([2, 4, 6, 8, 10, 12, 14, 16, 18]))
