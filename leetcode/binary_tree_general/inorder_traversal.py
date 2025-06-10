class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)  # Visit left subtree
        result.append(node.val)  # Visit root
        dfs(node.right)  # Visit right subtree

    dfs(root)
    return result
# Build tree:
#     1
#      \
#       2
#      /
#     3

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorder_traversal(root))  # Output: [1, 3, 2]
