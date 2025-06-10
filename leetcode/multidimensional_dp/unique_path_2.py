from typing import List

"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],
                       [0,1,0],
                       [0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        x_axis = len(obstacleGrid[0])
        y_axis = len(obstacleGrid)

        for i in range(y_axis):
            for y in range(x_axis):
                if obstacleGrid[i][y] == 1:
                    obstacleGrid[i][y] = -1
                    continue
                if i == 0 and y == 0:
                    obstacleGrid[i][y] = 1
                    continue
                if i == 0:
                    obstacleGrid[i][y] += 0 if obstacleGrid[i][y - 1] == -1 else obstacleGrid[i][y - 1]
                elif i > 0 and y == 0:
                    obstacleGrid[i][y] += 0 if obstacleGrid[i - 1][y] == -1 else obstacleGrid[i - 1][y]
                else:
                    obstacleGrid[i][y] += (0 if obstacleGrid[i][y - 1] == -1 else obstacleGrid[i][y - 1]) + (
                        0 if obstacleGrid[i - 1][y] == -1 else obstacleGrid[i - 1][y])
        return 0 if obstacleGrid[-1][-1] == -1 else obstacleGrid[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
