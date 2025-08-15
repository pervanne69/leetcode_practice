from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def is_valid_bst(root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], min_val=float("-inf"), max_val=float("inf")):
            if node is None: return True
            if not (min_val < node.val < max_val): return False
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)

        return is_valid(root)
