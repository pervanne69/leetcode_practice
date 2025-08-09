from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sol1(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    if root.val < low:
        return sol1(root.right, low, high)
    elif root.val > high:
        return sol1(root.left, low, high)
    else:
        return root.val + sol1(root.left, low, high) + sol1(root.right, low, high)


# root = [10,5,15,3,7,null,18], low = 7, high = 15
a = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, right=TreeNode(18)))

print(sol1(a, 7, 15))