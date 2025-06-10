"""
Example 1:
       3
   |       |
   9      100
        |     |
        10    11

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

f = TreeNode(3, TreeNode(9, TreeNode(val=5), TreeNode(val=4)), TreeNode(20, TreeNode(15), TreeNode(7)))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = root.left
        right = root.right
        return 1 + max(self.maxDepth(left), self.maxDepth(right))

print(Solution().maxDepth(f))