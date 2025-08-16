from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    global_max = -10 ** 9

    def dfs(node: Optional[TreeNode]):
        nonlocal global_max
        if not node:
            return 0
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)
        current_max = node.val + left_max + right_max
        global_max = max(global_max, current_max)
        return node.val + max(left_max, right_max)

    dfs(root)
    return global_max


print(maxPathSum(None))
