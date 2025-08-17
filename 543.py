from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    global_max = -10 ** 9

    def dfs(node: Optional[TreeNode]):
        nonlocal global_max
        if node is None:
            return 0

        left_max = dfs(node.left)
        right_max = dfs(node.right)
        global_max = max(global_max, left_max + right_max)

        return 1 + max(left_max, right_max)

    dfs(root)
    return global_max

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))



print(diameterOfBinaryTree(tree))