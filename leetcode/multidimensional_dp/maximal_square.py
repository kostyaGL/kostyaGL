"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_number = 0
        for x_axis in range(len(matrix)):
            for y_axis in range(len(matrix[0])):
                if matrix[x_axis][y_axis] == '0':
                    matrix[x_axis][y_axis] = 0
                else:
                    if x_axis == 0 or y_axis == 0:
                        matrix[x_axis][y_axis] = 1
                    else:
                        matrix[x_axis][y_axis] = min(
                            matrix[x_axis - 1][y_axis],
                            matrix[x_axis][y_axis - 1],
                            matrix[x_axis - 1][y_axis - 1]
                        ) + 1
                max_number = max(max_number, matrix[x_axis][y_axis])
        return max_number ** 2


print(Solution().maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))

print(Solution().maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "1", "1", "1"]]))

print(Solution().maximalSquare([["1", "0", "1", "0", "0"],
 ["1", "1", "1", "1", "1"],
 ["1", "1", "1", "1", "1"],
 ["1", "1", "1", "1", "1"],
 ["1", "1", "1", "1", "1"],
 ["1", "1", "1", "1", "1"]
 ]))
