from typing import List

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""


class Solution:
    def mark_diagonals(self, matrix, ln_matrix):
        for i in range(ln_matrix // 2):
            f = matrix[i][i]
            l = matrix[ln_matrix - i - 1][ln_matrix - i - 1]
            matrix[ln_matrix - i - 1][ln_matrix - i - 1] = f
            matrix[i][i] = l

        for start in range(1, ln_matrix - 1):
            step = 0
            ln = ln_matrix
            for i in range(start, ln_matrix):
                if ln_matrix - i - 1 > step:
                    f = matrix[step][i]
                    l = matrix[ln_matrix - i - 1][ln - 1]
                    matrix[ln_matrix - i - 1][ln - 1] = f
                    matrix[step][i] = l
                    fi = matrix[ln - 1][ln_matrix - i - 1]
                    li = matrix[i][step]
                    matrix[i][step] = fi
                    matrix[ln - 1][ln_matrix - i - 1] = li
                step += 1
                ln -= 1
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y, x = len(matrix), len(matrix[0])
        for i in range(y):
            step = 0
            while x // 2 > step:
                first_number = matrix[i][step]
                last_number = matrix[i][y - step - 1]
                matrix[i][y - step - 1] = first_number
                matrix[i][step] = last_number
                step += 1
        self.mark_diagonals(matrix, x)
        return matrix


print(Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5],
                                                                                             [14, 3, 4, 1],
                                                                                             [12, 6, 8, 9],
                                                                                             [16, 7, 10, 11]])
