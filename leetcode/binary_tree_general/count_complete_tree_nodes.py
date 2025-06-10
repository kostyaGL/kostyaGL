"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
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
arr = [1, 2, 3, 4, 5, 6]

# Build the tree
root = insert_level_order(arr, None, 0, len(arr))


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        return 1 + sum([self.countNodes(left), self.countNodes(right)])


print(Solution().countNodes(root))
