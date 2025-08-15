# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def to_bst(nums: List[int], left: int, right: int):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = to_bst(nums, left, mid - 1)
            node.right = to_bst(nums, mid + 1, right)

            return node

        return to_bst(nums, 0, len(nums) - 1)
