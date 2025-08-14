#Given the root of a binary tree, collect a tree's nodes as if you were doing this:
# • Collect all the leaf nodes.
# • Remove all the leaf nodes.
# • Repeat until the tree is empty.

from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def solution(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    helper(root, result)
    return result


def helper(root, result):
    if not root:
        return -1
    left = helper(root.left, result)
    right = helper(root.right, result)
    h = max(left, right) + 1
    if h == len(result):
        result.append([])
    result[h].append(root.val)
    return h



print(solution(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
