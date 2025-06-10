"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        # If k is larger than half of the number of days, we can treat it as infinite transactions
        if k >= len(prices) // 2:
            return self.maxProfitUnlimited(prices)

        # Initialize dp arrays for `hold` and `cash`
        hold = [-float('inf')] * (k + 1)
        cash = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                hold[j] = max(hold[j], cash[j - 1] - price)
                cash[j] = max(cash[j], hold[j] + price)

        return cash[k]

    def maxProfitUnlimited(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


# print(Solution().maxProfit(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
# print(Solution().maxProfit(3, [3, 3, 5, 0, 0, 3, 1, 4]))
