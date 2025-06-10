"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_sym(self, left, rigth):
        if not left and not rigth:
            return True
        if not left or not rigth:
            return False
        return left.val == rigth.val and self.is_sym(left.left, rigth.right) and self.is_sym(left.right, rigth.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        return self.is_sym(root.left, root.right)


f = TreeNode(1, TreeNode(2, TreeNode(val=3), TreeNode(val=4)), TreeNode(2, TreeNode(3), TreeNode(4)))
print(Solution().isSymmetric(f))
