from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104"""


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         min_coins = [amount + 1] * (amount + 1)
#         min_coins[0] = 0
#
#         for i in range(1, amount + 1):
#             for c in coins:
#                 if i - c >= 0:
#                     min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
#
#         return min_coins[-1] if min_coins[-1] != amount + 1 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Bitwise BFS.
            [1,2,5] amt = 11
            seen = 10000000000
        """

        step, seen = 0, 1 << amount
        while seen & 1 != 1:
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur == seen:
                return -1
            step, seen = step + 1, cur
        return step

print(Solution().coinChange(coins=[1, 2, 5], amount=11))
print(Solution().coinChange(coins=[2, 5, 10, 1], amount=27))
print(Solution().coinChange(coins=[2], amount=3))
print(Solution().coinChange(coins=[3, 7, 405, 436], amount=8839))