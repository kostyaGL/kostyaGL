"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for x in range(1, len(word1) + 1):
            for y in range(1, len(word2) + 1):
                if word1[x - 1] == word2[y - 1]:
                    dp[x][y] = dp[x - 1][y - 1]
                else:
                    dp[x][y] = min(
                        dp[x - 1][y] + 1,
                        dp[x - 1][y - 1] + 1,
                        dp[x][y - 1] + 1
                    )
        return dp[len(word1)][len(word2)]


print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("horse", "horse"))

# memoization
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         # word1 = "horse", word2 = "ros"
#         memo = {}
#
#         def dp(i, j):
#             if i == 0:
#                 return j  # Need to insert `j` characters of `word2` into `word1`
#             if j == 0:
#                 return i  # Need to delete `i` characters from `word1` to match empty `word2`
#
#             if (i, j) in memo:
#                 return memo[(i, j)]
#
#             if word1[i - 1] == word2[j - 1]:
#                 memo[(i, j)] = dp(i - 1, j - 1)  # Characters match, move to the next
#             else:
#                 insert = dp(i, j - 1)  # Insert the current character of `word2` into `word1`
#                 delete = dp(i - 1, j)  # Delete the current character of `word1`
#                 replace = dp(i - 1, j - 1)  # Replace character of `word1` with that of `word2`
#                 memo[(i, j)] = 1 + min(insert, delete, replace)  # Include operation cost
#
#             return memo[(i, j)]
#
#         return dp(len(word1), len(word2))
