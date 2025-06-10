"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp

        # Insert left child
        if temp is not None:
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # Insert right child
        if temp is not None:
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root


# List representing level-order traversal
arr = [5, 4, 8, 13, None, 12, 4, 7, 2, None, None, None, 1]

# Build the tree
root = insert_level_order(arr, None, 0, len(arr))


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        # Recur for the left and right subtrees with the reduced targetSum.
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))


# Testing the solution with targetSum = 22
print(Solution().hasPathSum(root, 22))  # Expected output: True or False depending on tree structure
